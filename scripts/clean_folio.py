import pandas as pd

df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv",
    encoding="latin1"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_folio.csv",
    index=False
)

print("Folio cleaned successfully")