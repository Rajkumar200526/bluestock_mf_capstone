Data Dictionary
01_fund_master.csv
Column	Type	Description
amfi_code	TEXT	Unique fund code
fund_house	TEXT	Mutual fund company
scheme_name	TEXT	Fund name
category	TEXT	Equity/Debt/Hybrid
expense_ratio_pct	REAL	Annual expense ratio
02_nav_history.csv
Column	Type	Description
amfi_code	TEXT	Fund code
date	DATE	NAV Date
nav	REAL	Net Asset Value
08_investor_transactions.csv
Column	Type	Description
investor_id	TEXT	Investor ID
transaction_date	DATE	Transaction date
transaction_type	TEXT	SIP/Lumpsum/Redemption
amount_inr	REAL	Investment Amount