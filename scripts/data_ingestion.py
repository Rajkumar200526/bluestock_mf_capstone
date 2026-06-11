"""
Data Ingestion Script

Author: Ampolu Raj Kumar
Project: Mutual Fund Analytics Platform

Description:
Reads all raw CSV files from the data/raw folder
and performs initial dataset inspection including:

- Shape
- Data Types
- Missing Values
- Sample Records
"""
import pandas as pd
import os

folder_path = "data/raw"

summary = []

files = os.listdir(folder_path)

for file in files:

    if file.endswith(".csv"):

        file_path = os.path.join(folder_path, file)

        try:
            df = pd.read_csv(file_path)
        except:
            df = pd.read_csv(file_path, encoding="latin1")

        summary.append([
            file,
            df.shape[0],
            df.shape[1]
        ])

# Save summary file
with open("reports/data_summary.txt", "w") as f:

    f.write("Dataset Name\tRows\tColumns\n")
    f.write("-" * 50 + "\n")

    for item in summary:

        f.write(
            f"{item[0]}\t{item[1]}\t{item[2]}\n"
        )

print("Data Summary Created Successfully!")