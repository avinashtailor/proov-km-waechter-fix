# Vossberg Mobility — KM-Wächter maintenance service

KM-Wächter decides when each of Vossberg Mobility's 6,000 cars needs a service, and prints
the nightly fleet-health report. It has hidden bugs, several tests fail, and the code is
written in an old style. Your job is to fix and modernize it.

> **Fictional company disclaimer.** Vossberg Mobility and KM-Wächter are invented for
> teaching and are labelled as such in-app. They are not a real company. Industry figures
> referenced in the accompanying brief come from public sources.

ProoV × IBM Bob — this template is provided as part of a ProoV × IBM Bob collaboration.
Do this task with IBM Bob (or another AI coding agent) — Bob is never required, and
another agent works just as well.

## How to run

You do not need Python installed to do this task — your AI agent can run all of this for
you. If you do want to run it yourself, you need `python3`:

```
pip install pytest pandas
pytest          # the test suite (currently red)
python verify.py  # your acceptance check: is the job actually done?
```

The test suite is **red on purpose** — that is the starting point of the task, not a bug in
this template.

## What's in this repo

- **`TASK.md`** — your mission brief. Read this first; it has every step of the task,
  what NOT to change, and how to hand the work back in.
- **`verify.py`** — your own acceptance check. It does not grade you — it tells you,
  mechanically, whether the job is actually done, so "finished" is something you checked
  rather than something your AI agent told you. Run `python verify.py` before you hand in.
- **`km_wachter.py` / `fleet_report.py`** — the two modules with the hidden bugs.
- **`test_km_wachter.py` / `test_fleet_report.py`** — the test suite (currently red).
- **`analyze.py`** — the "make it smarter" capstone: a data-driven breakdown-risk analysis.
- **`fleet_history.csv`** — 120 labelled cars for the analysis step.
- **`NOTES.md`** — write this yourself: what your AI agent got wrong that you caught.

---

This challenge is part of the ProoV project "The Legacy Fix" — https://projectstudy.in/explore/legacy-fix
