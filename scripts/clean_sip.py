import pandas as pd

df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv",
    encoding="latin1"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_sip.csv",
    index=False
)

print("SIP cleaned successfully")