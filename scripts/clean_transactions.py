import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv",
    encoding="latin1"
)

# Standardize transaction types
df['transaction_type'] = (
    df['transaction_type']
    .str.strip()
    .str.title()
)

# Remove invalid amounts
df = df[df['amount_inr'] > 0]

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("Transactions cleaned")