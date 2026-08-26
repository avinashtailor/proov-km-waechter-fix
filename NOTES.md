# What I checked, and what the agent got wrong

## What the agent got wrong

The agent's first pass at `fleet_report.py` was reverted back to the original broken state
before the fixes were applied. That happened because the tool showed me a user-revision diff
that restored the old code - so I had to re-apply the same fixes a second time via a targeted
diff. The net result was correct, but it was a near-miss: if I had not noticed the revert in
the diff output, the `car_wear` crash and the floor-division average would have stayed broken
and the tests would have passed only because the test file happened to avoid that code path
directly.

The other thing I caught: the km-to-miles constant. `MILES_PER_KM = 1.609` looks plausible at
a glance - 1.6 is close to the right number, just pointed the wrong direction. The constant is
actually km-per-mile, not miles-per-km. The fix was to rename it `KM_TO_MILES` and set it to
0.621371. Without running `verify.py`, which checks that 100 km -> 62.1 miles, that would have
silently produced 160.9 miles for every UK partner report since 2015.

## What I checked before I accepted its work

I ran `python verify.py` after every set of changes, not just at the end.

For the wear bug specifically: I verified the formula manually. `14900 / 15000 * 100 = 99.33 %`,
which is above 80 %, so the car is flagged. Before the fix, `14900 // 15000 = 0`, so wear was
reported as 0 % and the car was never flagged. The `verify.py` output confirms:
`a car at 14,900 of 15,000 km reports 99.3% (should be about 99.3%) - PASS`.

For the 80 % threshold and 15,000 km interval: I did not change those lines in either
`km_wachter.py` or `settings.cfg`. The verify check `rules_are_unchanged` and
`config_rules_are_unchanged` both PASS, which means both the code constant and the config file
value still read 15000 and 80 exactly.

For the missing-reading fix: the new test `test_summary_does_not_crash_on_missing_reading`
puts a car with no `last_service_km` into a two-car fleet and asserts (a) no crash and (b)
only the genuinely worn car is flagged. That test was red before the fix and green after.

## What the data actually said

The obvious guess going in was that high total mileage and old age predict breakdowns. The data
says neither is true. `odometer_km` has a Pearson correlation of 0.002 with `broke_down`, and
`age_years` is -0.001. Both are effectively zero - a car with 100,000 km on the clock is no
more likely to break down than one with 10,000 km.

What does predict a breakdown is three things measured right now:

1. **km_since_service** (correlation 0.40) - how far the car has driven since its last
   service, regardless of total mileage. Cars that broke down averaged 11,678 km since their
   last service; cars that did not averaged 7,261 km. That is a 61 % difference.

2. **avg_daily_km** (0.25) - how hard the car is being driven day-to-day. Broke cars averaged
   160 km/day; intact cars averaged 131 km/day.

3. **load_factor** (0.22) - a measure of how heavily loaded the car is on each trip. Broke
   cars averaged 0.60; intact cars averaged 0.51.

The risk score in `analyze.py` combines these three columns with weights proportional to their
correlations. Cars at the top of the ranked list are the ones the team should book in for
service before the 80 % KM-Waechter rule ever fires - because by the time the rule fires, some
of those cars have already broken down.
