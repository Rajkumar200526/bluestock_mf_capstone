import pandas as pd

df = pd.read_csv(
    "data/raw/05_category_inflows.csv",
    encoding="latin1"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_category_inflows.csv",
    index=False
)

print("Category Inflows cleaned successfully")