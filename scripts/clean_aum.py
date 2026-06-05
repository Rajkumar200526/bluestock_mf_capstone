import pandas as pd

df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv",
    encoding="latin1"
)

df['date'] = pd.to_datetime(
    df['date']
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_aum.csv",
    index=False
)

print("AUM cleaned successfully")