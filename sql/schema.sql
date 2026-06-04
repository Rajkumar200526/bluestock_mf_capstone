CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    expense_ratio_pct REAL
);

CREATE TABLE fact_nav (
    amfi_code TEXT,
    nav_date DATE,
    nav REAL,
    daily_return REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL
);

CREATE TABLE fact_performance (
    amfi_code TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    sharpe_ratio REAL,
    alpha REAL
);