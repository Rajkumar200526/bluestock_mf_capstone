import pandas as pd

df = pd.read_csv(
    "data/raw/01_fund_master.csv",
    encoding="latin1"
)

df = df.drop_duplicates()

df['launch_date'] = pd.to_datetime(
    df['launch_date']
)

df.to_csv(
    "data/processed/clean_fund_master.csv",
    index=False
)

print("Fund Master cleaned successfully")