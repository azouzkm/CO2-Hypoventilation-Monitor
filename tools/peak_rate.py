"""Offline breathing rate by peak counting (CR-4, ER-7). Not used live by the device.

Each exhale reaching the sensor speeds up the rise of the CO2 reading for a moment, so the slope
of the reading (ppm per second) shows one bump per breath even when the reading itself looks like
one smooth curve. This script:
  1. takes the 1 reading/s CO2 values over a breathing window,
  2. works out the slope (reading minus the reading 1 s earlier),
  3. removes the slow trend (slope minus its 9 s moving mean),
  4. counts the bumps (local maxima above MIN_BUMP ppm/s, at least MIN_GAP_S apart),
  5. breathing rate = 60 / median time between bumps (breaths/min).
It answers "not resolved" when it finds fewer than MIN_PEAKS bumps or the gaps are irregular
(coefficient of variation above MAX_CV), rather than guessing.

    python3 tools/peak_rate.py                 every test 5 run and the 22 Oct paced run
Writes data/runs/peak_rate_results.csv.
"""
import csv, json, re, statistics as st

MIN_BUMP = 2.0     # ppm/s above the local trend
MIN_GAP_S = 2      # bumps closer than this are one breath (faster than 30/min is not counted)
MIN_PEAKS = 4
MAX_CV = 0.35


def rate(values):
    """values: CO2 readings at 1 per second. Returns (rate or None, bump indices, why)."""
    s = [b - a for a, b in zip(values, values[1:])]
    trend = [st.mean(s[max(0, i - 4):i + 5]) for i in range(len(s))]
    d = [a - b for a, b in zip(s, trend)]
    bumps = []
    for i in range(1, len(d) - 1):
        if d[i] > d[i - 1] and d[i] >= d[i + 1] and d[i] > MIN_BUMP:
            if bumps and i - bumps[-1] < MIN_GAP_S:
                continue
            bumps.append(i)
    if len(bumps) < MIN_PEAKS:
        return None, bumps, "fewer than %d bumps" % MIN_PEAKS
    gaps = [b - a for a, b in zip(bumps, bumps[1:])]
    cv = st.pstdev(gaps) / st.mean(gaps)
    if cv > MAX_CV:
        return None, bumps, "irregular gaps (CV %.2f)" % cv
    return 60.0 / st.median(gaps), bumps, "%d bumps, gaps CV %.2f" % (len(bumps), cv)


def hms(x):
    h, m, s = map(int, x.split(":"))
    return h * 3600 + m * 60 + s


def run_log(path, present_s):
    """A test 5 log: window from the breath reaching the sensor to the stop + the same delay."""
    pts, cues, stop = [], [], None
    for line in open(path):
        m = re.match(r"(\d\d:\d\d:\d\d)\s+(.*)", line)
        if not m:
            continue
        t, body = hms(m.group(1)), m.group(2)
        if body.startswith("## CUE"):
            cues.append(t)
        elif body.startswith("## STOP"):
            stop = t
        elif body.startswith("{"):
            try:
                d = json.loads(body)
            except ValueError:
                continue
            if d.get("ppm") is not None:
                pts.append((t, d["ppm"]))
    lag = present_s
    return [p for t, p in pts if cues[0] + lag <= t <= stop + lag and p < 5000]


if __name__ == "__main__":
    out = []
    rows = list(csv.DictReader(open("data/2026-10-22_session2_readings.csv")))
    br = [int(r["co2_ppm"]) for r in rows if r["label"] == "rhythmic_run_1_breathing"]
    rr, bumps, why = rate(br)
    out.append(("2026-10-22 paced run (open air, no line)", 15, rr, len(br), why))
    for r in csv.DictReader(open("data/runs/test5_summary.csv")):
        v = run_log("data/raw/" + r["log"], int(r["present_s"]))
        rr, bumps, why = rate(v)
        out.append(("test 5 valid run %s (0.5 m line, sealed cell)" % r["valid_run"], 15, rr, len(v), why))
    with open("data/runs/peak_rate_results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["recording", "true_rate_per_min", "peak_rate_per_min", "seconds_used", "why"])
        for name, true, rr, n, why in out:
            w.writerow([name, true, "" if rr is None else round(rr, 1), n, why])
            print("%-48s true %d  peak-count %-6s %s" % (name, true, "--" if rr is None else "%.1f" % rr, why))
