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

## Test 5 setup runs (3 Nov), kept, not scored
- run_2026-11-03_175400_mask-run01.log: test 5 setup, non-rebreather mask with the tube on its O2 connector, one side hole left open. Green only at 70 s (breath 17); reading still rising after the stop, no red. Excluded at the tester's request; the 10 scored runs start fresh.
- run_2026-11-03_175815_bare-run01.log: test 5 setup, bare tube end 3-5 cm from the mouth, 15 breaths. Green at 21 s (breath 6); reached 5,000 ppm (top of the sensor) before the stop, so no red; TECHNICAL "top of range" after 30 s. Excluded at the tester's request.
- run_2026-11-03_180645_t5-run01.log: test 5, non-rebreather mask, 10 breaths. Green only at 63 s (after the last breath), peak 2,993 ppm, no red. Excluded at the tester's request: the syringe was not pulled steadily.
- run_2026-11-03_181104_t5-run01.log: test 5 setup, non-rebreather mask with both side holes covered, steady pull, 10 breaths. Started at 1,673 ppm, still falling (not flushed to room level). Nothing for 24 s, then a sudden jump: green at 26 s (breath 7), 5,000 ppm (top of the sensor) at the stop, no red; TECHNICAL "top of range" after 30 s. Third mask run that failed both scores; the mask was dropped and the 10 scored runs use the bare tube.

## Test 5 scored set (4 Nov)
- run_2026-11-04_190938_t5-run03.log: test 5, excluded for a protocol deviation: the person pulling the syringe was distracted and the pull ran below the protocol pace (first rise about 8 s after the first cue, about 5 s in runs 1-2). Repeated as a new t5-run03.
- run_2026-11-04_191500_t5-run04.log: test 5, excluded for a protocol deviation reported during the run: the person pulling the syringe was distracted and the pull stopped (CO2 fell from breath 8 while breathing continued). Repeated.

## Test 4 (blocked line): pre-seal trial excluded (decided 4 Nov)
- The pinch at about 18:25:40 on 2 Nov in data/raw/co2_2026-11-02_175529.log is excluded from the ER-6 result: it was done before the leak at the sensor's wire exit was sealed (22:16), so the pinch may not have stopped all flow. The log stays in data/raw because it also holds tests 1, 2, 3 and 7. ER-6 is reported from the sealed trial on 3 Nov with the 2.1 m line (operator confirmed; pinch 00:42:10, CRITICAL 00:42:45, data/raw/co2_2026-11-03_003113.log).
