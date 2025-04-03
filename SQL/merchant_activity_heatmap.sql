-- Merchant transaction heatmap
SELECT
    merchant_id,
    DATE_TRUNC('HOUR', timestamp) AS hour,
    COUNT(*) AS transactions,
    SUM(amount_usd) AS revenue
FROM finance_db.etl.transactions
GROUP BY merchant_id, hour
ORDER BY hour DESC;
