"""Turns one line from the monitor into a dict the service can use.

The board (firmware v0.5 and later) prints two lines per second: one for people and one JSON object
for this service (interface IF-6). Older firmware printed only the line for people, so that one is
understood too: recorded logs from 22 to 25 Oct can be replayed into the dashboard. Firmware v0.6
adds the breathing rate (CR-4: "rr", "rr_why", "advisory") and the safety clip on the sampling line
(CR-3: "line", true while the line is on); on its text line they read "RR 15.2" (or "RR --") and
"LINE OFF".

    {"v": "0.6", "t": 312, "ppm": 1814, "cr1": "PRESENT", "rr": 15.2, "line": true, ...}  -> "sample" (JSON)
    t=  312 s  CO2  1814 ppm  |#########....|  PRESENT    NORMAL       RR 15.2            -> "sample" (text)
    t=  315 s  no answer from sensor  FAULT      TECHNICAL                 -> kind "sample" (text)
    >>> ALARM CRITICAL: CO2 lost: fell 108 ppm from 1814 in under 20 s <<<  -> kind "banner"
    Team 6 CO2 monitor v0.5 - CR-1 present/absent ...                     -> kind "boot"

Pure Python, no I/O.
"""
from __future__ import annotations

import json
import re

CR1_STATES = ("WARMING UP", "ABSENT", "PRESENT", "FAULT")
DISPLAYS = ("STANDBY", "NORMAL", "ADVISORY", "CRITICAL ACK", "CRITICAL BACK", "CRITICAL", "TECHNICAL")

_CR1 = "|".join(CR1_STATES)
_SHOW = "|".join(DISPLAYS)
_READING = re.compile(r"^t=\s*(\d+) s\s+CO2\s+(\d+) ppm\s+\|[#.]*\|\s+(%s)(?:\s+(%s))?" % (_CR1, _SHOW))
_NO_ANSWER = re.compile(r"^t=\s*(\d+) s\s+no answer from sensor\s+(%s)(?:\s+(%s))?" % (_CR1, _SHOW))
_BANNER = re.compile(r"^>>> (.*) <<<$")
_BOOT = re.compile(r"Team 6 CO2 monitor v(\d+\.\d+)")
_RR = re.compile(r"\bRR (--|\d+(?:\.\d+)?)(?=\s|$)")
_CLOCK = re.compile(r"^\d\d:\d\d:\d\d  ")   # "HH:MM:SS  " put in front of each line by the Mac tools
# CircuitPython also writes terminal control codes: its status bar ("ESC]0;Wi-Fi: off | code.py ESC\")
# and line clearing ("ESC[2K"). They are not part of what the program printed.
_ESCAPES = re.compile(r"\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)|\x1b\[[0-9;?]*[A-Za-z]")


def clean(line: str) -> str:
    """The line without terminal control codes."""
    return _ESCAPES.sub("", line)


def alarm_of(show: str | None) -> str | None:
    """The alarm state behind what the ring shows: CRITICAL ACK and CRITICAL BACK are CRITICAL."""
    if show is None:
        return None
    return "CRITICAL" if show.startswith("CRITICAL") else show


def strip_clock(line: str) -> str:
    """Drop the Mac's "HH:MM:SS  " prefix that the raw logs carry."""
    return line[10:] if _CLOCK.match(line) else line


def _number(x):
    """A number from the JSON line, or None (also for anything that is not a number)."""
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    return float(x)


def _rate_and_line(line: str) -> dict:
    """The breathing rate and the sampling line from a text line (firmware v0.6 and later)."""
    m = _RR.search(line)
    rr = None if m is None or m.group(1) == "--" else float(m.group(1))
    if "LINE OFF" in line:
        connected = False
    else:
        connected = True if m else None          # older firmware had no safety clip: not known
    return {"rr": rr, "rr_why": None, "advisory": None, "line": connected}


def parse_line(line: str) -> dict:
    line = clean(line).strip()
    if line.startswith("{"):
        try:
            d = json.loads(line)
        except ValueError:
            return {"kind": "garbled", "text": line}
        if not isinstance(d, dict) or "t" not in d:
            return {"kind": "garbled", "text": line}
        show = d.get("show")
        return {
            "kind": "sample", "source": "json", "fw": d.get("v"),
            "t": d.get("t"), "ppm": d.get("ppm"),
            "cr1": d.get("cr1"), "cr1_why": d.get("cr1_why"),
            "alarm": d.get("alarm") or alarm_of(show), "show": show, "why": d.get("why"),
            "acked": bool(d.get("acked")), "latched": bool(d.get("latched")),
            "press": int(d.get("press") or 0), "hold": int(d.get("hold") or 0),
            "dash_ack": int(d.get("dash_ack") or 0),
            "rr": _number(d.get("rr")), "rr_why": d.get("rr_why"), "advisory": d.get("advisory"),
            "line": d.get("line") if isinstance(d.get("line"), bool) else None,
        }
    m = _READING.match(line)
    if m:
        show = m.group(4)
        return dict({"kind": "sample", "source": "text", "fw": None, "t": int(m.group(1)), "ppm": int(m.group(2)),
                     "cr1": m.group(3), "cr1_why": None, "alarm": alarm_of(show), "show": show, "why": None,
                     "acked": show == "CRITICAL ACK", "latched": bool(show and show.startswith("CRITICAL")),
                     "press": 0, "hold": 0, "dash_ack": 0}, **_rate_and_line(line))
    m = _NO_ANSWER.match(line)
    if m:
        show = m.group(3)
        return dict({"kind": "sample", "source": "text", "fw": None, "t": int(m.group(1)), "ppm": None,
                     "cr1": m.group(2), "cr1_why": None, "alarm": alarm_of(show), "show": show, "why": None,
                     "acked": show == "CRITICAL ACK", "latched": bool(show and show.startswith("CRITICAL")),
                     "press": 0, "hold": 0, "dash_ack": 0}, **_rate_and_line(line))
    m = _BANNER.match(line)
    if m:
        return {"kind": "banner", "text": m.group(1)}
    m = _BOOT.search(line)
    if m:
        return {"kind": "boot", "fw": m.group(1), "text": line}
    return {"kind": "other", "text": line}


def quality(sample: dict) -> str:
    """How far a reading can be trusted, for the readings table."""
    ppm = sample.get("ppm")
    if ppm is None:
        return "no_answer"
    if sample.get("cr1") in ("WARMING UP", "FAULT"):
        return "not_trusted"
    if ppm <= 400:
        return "floor"
    if ppm >= 5000:
        return "top_of_range"
    return "ok"
