# Test 5 protocol (fixed Wed 4 Nov 2026, 18:55, before the first scored run)

Same conditions for all 10 scored runs (labels t5-run01 .. t5-run10). Nothing below changes between runs.

## Set-up
- Sampling line: 0.5 m (the bench line ER-1 was set for; the cost of a longer line is measured in test 6), 3/16" ID vinyl, on SAMPLE. Syringe: MotoMaster 200 mL on VENT. Sealed cell (finger test passed).
- Tube end held 10 cm (a hand's width) in front of the mouth, fixed to a ruler held at the chin. No mask.
- One person breathes, the same person pulls for all 10 runs (or note who pulls in each row).

## Each run
1. Flush: tube end away from anyone's face, pull until the reading is steady (not falling) near room level, alarm on STANDBY. Empty the syringe off the line.
2. Start: `bash tools/scripted_run.sh --rate 15 --breaths 10 --rest 60 --label t5-runNN`
3. Pull steadily, one 10 mL mark every 5 s (about 2 mL/s). Start about 10 s before the first "breathe" cue, keep going through the stop and the 60 s rest. No syringe swap during the run; if the syringe is full after the red alarm, stop pulling (scoring is not affected).
4. Breathe normally in time with the cues (10 breaths at 15/min, nose or mouth kept the same across runs), then stop on "stop" and hold still, mouth closed, away from the tube end, through the rest.

## Scoring (automatic, data/runs/results.csv)
- ER-1 pass: PRESENT by breath 3 after the first cue.
- ER-2 pass: CRITICAL within 30 s of the stop cue.
- Breathing rate (CR-4): recorded as shown (expected "--", known sensor limit).

## Exclusion rule (decided before the runs)
A scored run is excluded only for a protocol deviation noted at the time: not flushed to a steady baseline, pull stopped or swapped, tube moved, talking or another person breathing near the tube, script not started. A run is never excluded because it failed. A run that reaches 5,000 ppm (top of the sensor) is kept and scored as it is, with saturation recorded as the cause of any ER-2 fail; the distance is not changed between scored runs. Excluded runs are moved to data/raw/excluded/ with the reason and replaced by a new run; the replacements are reported.

## Setup runs (not scored, kept in data/raw/excluded/)
Three mask runs and one bare-tube run at 3-5 cm on 3 Nov, 17:54-18:12, used to choose this method: the mask held the breath back (green at 26-70 s) and the 3-5 cm distance and the sealed mask drove the sensor to 5,000 ppm, so no red after the stop.

## Run notes (written during the session)
- t5-run01: peak 5,000 ppm from breath 8 to 16 s after the stop (TECHNICAL "top of range" 4 s); red still 24 s after the stop.
- t5-run02: peak 2,228 ppm; baseline drifting down about 20 ppm over the 24 s before the first cue.
- t5-run03 (first attempt, 19:09): excluded for a protocol deviation: the operator reported the pull started slower than the protocol pace (first rise about 8 s vs about 5 s in runs 1-2). Log in data/raw/excluded/.
- t5-run04 (first attempt, 19:15): excluded for a protocol deviation reported during the run: the person pulling was distracted and the pull stopped (CO2 fell from breath 8 while breathing continued). Log in data/raw/excluded/.
- Valid runs are numbered 1-10 in time order in the report; the labels t5-run03/04 at 19:21 and 19:24 are valid runs 3 and 4.
- t5-run03: peak 5,000 ppm from breath 10 to 10 s after the stop (no TECHNICAL); baseline rising about 30 ppm over the 24 s before the first cue.
- t5-run04: peak 3,598 ppm, a plateau from breath 7 to the stop (no saturation); baseline flat about 860 ppm.
- t5-run05: at 5,000 ppm from 1 s before the stop to 28 s after (TECHNICAL top of range for 1 s at 19:35:03); red 33 s after the stop: the ER-2 fail is caused by saturation.
- t5-run06 (valid run 6): peak 3,526 ppm, no saturation; small dip at breaths 9-10 (3,507 to 3,412) without an alarm; baseline about 985-990 ppm.
- t5-run07 (valid run 7): peak 4,167 ppm, no saturation; baseline rising about 50 ppm over the 24 s before the first cue (room air near the tube end), which may have brought green slightly earlier.
- t5-run08 (valid run 8): peak 3,756 ppm, no saturation; baseline flat about 880 ppm; the reading began to fall slightly from breath 9 (3,755 to 3,677 at the stop) with no alarm during breathing, which brought the red early (8 s after the stop).
- t5-run09 (valid run 9): peak 4,595 ppm, no saturation; baseline drifting down about 27 ppm before the first cue; the reading began to fall at breath 10; red 9 s after the stop.
- t5-run10 (valid run 10): peak 3,328 ppm, no saturation; baseline about 920-930 ppm, drifting down slightly; red 13 s after the stop.
