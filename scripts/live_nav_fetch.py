import requests
import pandas as pd
import os

# HDFC Top 100 Fund
scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

# Convert NAV history into DataFrame
nav_df = pd.DataFrame(data["data"])

# Create folder if not exists
os.makedirs("data/raw", exist_ok=True)

# Save CSV
nav_df.to_csv(
    "data/raw/hdfc_top100_nav.csv",
    index=False
)

print("File Saved Successfully!")
print("Rows:", len(nav_df))