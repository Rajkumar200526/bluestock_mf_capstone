import pandas as pd

scorecard = pd.read_csv(
    "outputs/fund_scorecard.csv"
)

fund = pd.read_csv(
    "data/raw/01_fund_master.csv",
    encoding="latin1"
)

df = scorecard.merge(
    fund,
    on="amfi_code"
)

risk = input(
    "Enter Risk Level (Low/Moderate/High): "
)

result = df[
    df['risk_category']
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

result = result.sort_values(
    'sharpe_ratio',
    ascending=False
)

print(
    result[
        ['scheme_name','sharpe_ratio']
    ].head(3)
)