-- 1. Top 5 Fund Houses by AUM

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV per Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. Total SIP by State

SELECT
state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 4. Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 5. Highest NAV Funds

SELECT
amfi_code,
MAX(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 6. Category Wise Funds

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 7. Transaction Type Count

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. KYC Status Count

SELECT
kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- 9. Average Expense Ratio

SELECT
AVG(expense_ratio_pct)
FROM dim_fund;

-- 10. Top 10 Investors

SELECT
investor_id,
SUM(amount_inr)
FROM fact_transactions
GROUP BY investor_id
ORDER BY SUM(amount_inr) DESC
LIMIT 10;