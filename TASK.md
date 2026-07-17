# Your mission — fix and modernize KM-Waechter

You are a junior engineer at Vossberg Mobility. This repo decides when 6,000 sports cars get
serviced and prints the nightly health report. It is broken, and the code is dated.

Do this with IBM Bob (or another AI coding agent). You do NOT need the Proov tab open while you
work. Everything you need is in this file. Come back when the repo is green.

## You do not need to set anything up
You do not need Python installed. You do not need to know pytest or pandas. Your agent runs the
code, runs the tests, and can push to GitHub for you. Your job is to DIRECT it and to CHECK it —
that is the actual skill here, and it is the one being graded.

## What to do
1. Run the tests. Several fail. Read why each one fails.
2. Fix the wear bug in km_wachter.py so a nearly-worn car is flagged.
3. Fix the missing-reading bug so a car with no last-service reading is not falsely flagged.
4. Fix fleet_report.py: it crashes on a car with no reading, and its average wear is wrong.
5. Have Bob ADD the missing test noted in test_fleet_report.py (a car with no reading must not
   crash the report), and make it pass.
6. Modernize the style across both files: f-strings, type hints, short docstrings, and remove
   the "== True" and the needless else.
7. Make it smarter (this is the part you show off). Open analyze.py. With Bob and pandas, use
   fleet_history.csv (120 cars, and we know which ones later broke down) to find which factors
   actually predict a breakdown, then print a risk score for each car so the team fixes the risky
   ones BEFORE the 80 percent rule would ever flag them.

   Be careful here. The obvious column is total mileage. Check whether it actually separates the
   cars that broke down from the ones that did not — a lot of juniors report "older, higher-mileage
   cars break down" and the data does not say that. Follow the data, not the assumption.

8. Write NOTES.md: in your own words, what did the agent get WRONG that you caught? Every agent
   gets something wrong on a job this size. If you genuinely caught nothing, say what you checked
   and how you convinced yourself it was right.

## Do not change
- The 15000 km service interval.
- The 80 percent flag threshold.
- What the service is meant to decide.

## Done when
Run your own acceptance check:

```
python verify.py
```

It prints PASS or FAIL for each requirement. Do not hand in until it is all PASS. That is the
difference between "the AI said it was finished" and "I checked".

## About your free trial
The whole mission is about 8 to 12 agent prompts, and the free Bob trial gives you 40 Bobcoins,
which is comfortably more than that job needs (trial terms as at the time of writing, and they can
change). If you do run low: do steps 1 to 6 with the agent, and do the analysis in step 7 yourself
or with any other agent. Nothing here depends on one particular tool.

## Hand it back
Push this repo to your OWN public GitHub, then paste the link into Proov. Bob can push it for you —
ask it: "initialise a git repo, commit everything, and push to a new PUBLIC GitHub repo on my
account, then give me the link." If you cannot use GitHub, paste your fixed files instead.
