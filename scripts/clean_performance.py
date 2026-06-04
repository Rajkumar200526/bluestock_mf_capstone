import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv",
    encoding="latin1"
)

numeric_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct',
    'alpha',
    'beta',
    'sharpe_ratio'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Performance data cleaned")