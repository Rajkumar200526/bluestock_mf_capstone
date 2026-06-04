import requests
import pandas as pd
import os

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

os.makedirs("data/raw", exist_ok=True)

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{fund_name}.csv"

        df.to_csv(file_name, index=False)

        print(f"{fund_name} saved successfully")
    else:
        print(f"Failed: {fund_name}")