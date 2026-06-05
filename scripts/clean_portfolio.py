import pandas as pd

df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv",
    encoding="latin1"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_portfolio.csv",
    index=False
)

print("Portfolio cleaned successfully")