# Breathing-rate bench run (ER-7, ER-8), 4 Nov 2026

Setup, fixed before the run: 0.5 m line on SAMPLE, tube end 15 cm from the mouth, no mask; 200 mL syringe on VENT pulled at about 1 mL/s (one 10 mL mark every 10 s), no swap; `bash tools/rate_run.sh --plan 10:120 --rest 30 --label rr-run01` (10 breaths/min for 120 s, 30 s rest).

- rr-run01 (20:55, valid): green 13 s after the first cue; reading reached 5,000 ppm (the fitted sensor's top of range) at about breath 6 and stayed there to the end; TECHNICAL "reading at the top of the scale for 30 s: the sensor cannot see breaths" at 20:57:20. No breathing rate shown at any time ("breaths cut off" while saturated; before that "rhythm too small to trust"); no wrong rate shown; no ADVISORY; no false CRITICAL.

Key constraint (manufacturer data): the fitted MH-Z19C is the 0-5,000 ppm version. Winsen lists 2,000 / 5,000 / 10,000 ppm versions (10,000 "optional"), and the MH-Z19C manual documents no command to change the range (only read CO2 and self-calibration on/off), so the cap cannot be raised in software. Exhaled breath is about 40,000-50,000 ppm, so even a 10,000 ppm module would need a fixed dilution.
