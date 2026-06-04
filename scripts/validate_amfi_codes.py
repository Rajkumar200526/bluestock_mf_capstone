import pandas as pd

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv",
    encoding="latin1"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv",
    encoding="latin1"
)

missing_codes = set(
    fund_master['amfi_code']
) - set(
    nav_history['amfi_code']
)

print("Missing Codes:")
print(missing_codes)

print("\nTotal Missing:")
print(len(missing_codes))