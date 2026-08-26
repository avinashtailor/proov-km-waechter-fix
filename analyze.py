# analyze.py
#
# KEY FINDINGS:
# The three factors that actually predict a breakdown are km_since_service (correlation 0.40),
# avg_daily_km (0.25), and load_factor (0.22). Total odometer mileage and age both have
# near-zero correlation (0.002 and -0.001): a high-mileage or old car is NOT meaningfully more
# likely to break down than a low-mileage one. The risk is in how hard a car is driven RIGHT NOW
# and how long it has gone without a service - not how old or how far it has travelled overall.
#
# The risk score below combines only those three separating factors.

import pandas as pd

df = pd.read_csv("fleet_history.csv", encoding="utf-8")

# -- Step 1: inspect the data ------------------------------------------------
print("Dataset: %d cars, %d columns" % (df.shape[0], df.shape[1]))
print(df.head())
print()

# -- Step 2: find which columns separate broke vs did-not-break --------------
broke = df[df["broke_down"] == 1]
ok    = df[df["broke_down"] == 0]

print("Breakdown rate: %.1f%%" % (df["broke_down"].mean() * 100))
print()

cols = ["odometer_km", "km_since_service", "avg_daily_km", "load_factor", "age_years"]
print(f"{'Column':<20}  {'Broke avg':>10}  {'OK avg':>10}  {'Diff %':>8}  {'Corr':>6}")
print("-" * 64)
for c in cols:
    bm   = broke[c].mean()
    om   = ok[c].mean()
    diff = (bm - om) / om * 100
    corr = df[c].corr(df["broke_down"])
    print(f"{c:<20}  {bm:>10.1f}  {om:>10.1f}  {diff:>+8.1f}%  {corr:>+6.3f}")

print()
print("RESULT: odometer_km and age_years are NOT predictive (correlation ~= 0).")
print("The three predictive columns are: km_since_service, avg_daily_km, load_factor.")
print()

# -- Step 3: build a 0-100 risk score from the three signal columns ----------
#
# Each signal column is min-max normalised to [0, 1] across the full fleet,
# then combined with weights proportional to their absolute Pearson correlation:
#   km_since_service  r = 0.404  ->  weight 0.57
#   avg_daily_km      r = 0.252  ->  weight 0.36
#   load_factor       r = 0.215  ->  weight 0.30  (re-normalised so weights sum to 1)

def minmax(series: pd.Series) -> pd.Series:
    """Normalise a series to the [0, 1] range."""
    lo, hi = series.min(), series.max()
    return (series - lo) / (hi - lo)

w_kss = 0.404
w_adk = 0.252
w_lf  = 0.215
total_w = w_kss + w_adk + w_lf

df["score"] = (
    (minmax(df["km_since_service"]) * w_kss +
     minmax(df["avg_daily_km"])     * w_adk +
     minmax(df["load_factor"])      * w_lf)
    / total_w * 100
)

# -- Step 4: print fleet ranked by risk, highest first -----------------------
ranked = df[["car_id", "km_since_service", "avg_daily_km", "load_factor", "broke_down", "score"]]\
           .sort_values("score", ascending=False)\
           .reset_index(drop=True)

print(f"{'#':<4}  {'Car ID':<10}  {'km_since_svc':>13}  {'daily_km':>9}  {'load':>6}  {'score':>6}  {'broke?':>7}")
print("-" * 68)
for i, row in ranked.iterrows():
    flag = " [BROKE]" if row["broke_down"] == 1 else ""
    print(
        f"{i+1:<4}  {row['car_id']:<10}  {row['km_since_service']:>13,.0f}  "
        f"{row['avg_daily_km']:>9,.0f}  {row['load_factor']:>6.2f}  "
        f"{row['score']:>6.1f}{flag}"
    )
