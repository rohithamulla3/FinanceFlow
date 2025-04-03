-- Daily transaction volume and total value
SELECT
    DATE_TRUNC('DAY', timestamp) AS day,
    COUNT(*) AS transaction_count,
    SUM(amount_usd) AS total_value_usd
FROM finance_db.etl.transactions
GROUP BY 1
ORDER BY 1 DESC;
