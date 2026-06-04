import pandas as pd

df = pd.read_csv(
    "data/raw/02_nav_history.csv",
    encoding="latin1"
)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort values
df = df.sort_values(
    ['amfi_code', 'date']
)

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid NAV
df = df[df['nav'] > 0]

print("Rows:", len(df))

df.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)

print("Clean NAV saved")