# Excluded runs (kept, not scored)

- run_2026-11-02_214353_len100-t1.log: test 6, 1 m tube. The tester breathed out continuously until the stop cue instead of one short breath; repeated as a new len100-t1.
- run_2026-11-02_214936_len100-t1.log: test 6, 1 m tube, second attempt; excluded at the tester's request: the breath probably missed the tube end (breathed in the wrong direction); repeated.
- run_2026-11-02_215255_len100-t1.log: test 6, 1 m tube, third attempt; excluded: people talking near the tube during the run (nearby breath contaminates the sample); repeated.
- run_2026-11-02_215548_len100-t1.log: test 6, 1 m tube, fourth attempt; excluded: no breath reached the sensor (reading flat ~1,050–1,090 ppm), set-up problem under investigation.
- run_2026-11-02_220157_len100-t1.log: test 6, 1 m tube, fifth attempt; excluded: no breath reached the sensor (flat ~1,250 ppm); air leak found, syringe suspected (pull easy, push hard with SAMPLE blocked).
- run_2026-11-02_220631_len100-t1.log and run_2026-11-02_221011_len100-t1.log: test 6, 1 m tube; excluded: air leak at the sensor's wire exit (cell/box) diluted the sample (rise only +170/+182 ppm, onset 6 s vs 18 s).

Leak check: run_2026-11-02_223427_len050-leakcheck.log (kept in data/raw) repeated the 0.5 m trial with the leak still open: rise +201 ppm, onset 12 s, PRESENT 16 s, against +504 to +1,332 ppm and 7-10 s for the three 0.5 m trials at 21:23-21:37. So the leak was not open during those trials; it most likely opened during the tube swap (21:38-21:44). Leak found 22:16 at the wire exit.
- run_2026-11-02_235159_len050s-t1.log: test 6, 0.5 m tube after sealing, first try; repeated: breath arrived at 11 s, later than through 1 m (7 s), suspected leak at the 0.5 m tube's joint or slower pulling (onset 11 s, PRESENT 13 s, rise +704, red 44 s).
- run_2026-11-02_234021_len100-t1.log: not started by the script (no breath cue); kept for the record.
- run_2026-11-02_234050_len100-t1.log, run_2026-11-02_234428_len100-t2.log, run_2026-11-02_234717_len100-t3.log: test 6, 1 m tube, sealed, syringe pulled by a different person (the helper); removed from the main set so every length has the same operator. Their result is kept as a finding: breath arrived at 7, 7, 8 s against 13, 18, 20 s for AKM on the same tube, so the hand draw depends on who pulls.

Not excluded but not in the test 6 result: the 0.5 m trials made before the leak was sealed (run_2026-11-02_212323_len050-t1, 213038_len050-t2, 213647_len050-t3; rises +504 to +1,332 ppm, partly diluted) and two runs the script did not start or that had no breath (212039_len050-t1: board warming up; 212812_len050-t2: stopped, no breath). They stay in data/raw as the 'before the seal' record. The test 6 result uses the sealed runs listed in data/runs/tube_length_results.csv.
