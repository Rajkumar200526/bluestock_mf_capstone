import pandas as pd

df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv",
    encoding="latin1"
)

df['date'] = pd.to_datetime(
    df['date']
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_benchmark.csv",
    index=False
)

print("Benchmark cleaned successfully")