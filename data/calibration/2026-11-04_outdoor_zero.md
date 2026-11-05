# One-point zero against outdoor air (ER-4), Wed 4 Nov 2026

Reference: NOAA GML monthly mean CO2 at Mauna Loa, 426.07 ppm (September 2026; gml.noaa.gov/ccgg/trends), taken as 426 ppm, with 0 to +30 ppm allowed for urban air (Montreal). The simulation-lab capnograph was not available before submission.

Set-up: box, laptop and syringe outdoors at night (cold); sealed flow-cell; 2.1 m line on SAMPLE, tube end at full length upwind of the operator, at least 2 m from any face; syringe on VENT, 40 mL pulled every 2 min. Board replugged at 21:24 (USB link lost when carried outside): warm-up placeholder (500 ppm) until 21:25:45. Analysis window fixed before looking at the result: 21:28:00 onwards (after warm-up and first flushes); recording to 21:37:32. Log: data/raw/co2_2026-11-04_212406.log.

Result (21:28:00 to 21:37:32, 573 readings, no alarms):
- mean 720 ppm, median 722, SD 16 ppm, range 689 to 751 ppm
- drift (least-squares slope) -2.3 ppm/min, about -23 ppm over 10 min: within the ER-4 criterion of +/-50 ppm over 10 min
- zero offset: 720 - 426 = +294 ppm (+264 to +294 allowing for urban air)

Comparison with test 1 (2 Nov, by a window, before the wire-exit leak was sealed): mean 756 ppm. Sealed and fully outdoors the reading is 720 ppm, so the offset is mainly in the sensor itself (at most about 36 ppm came from the leak or the window set-up), not from the leak.

Correction applied in the analysis (not on the sensor; its zero command was not used): true CO2 = reading - 294 ppm. Above the zero, accuracy is taken from the manufacturer: +/-(50 ppm + 5 % of reading) (Winsen MH-Z19C datasheet). The alarms work on changes in the reading (rises and falls), so the offset does not change any alarm result. A multi-point calibration curve with residuals needs a reference gas or the capnograph: future work.
