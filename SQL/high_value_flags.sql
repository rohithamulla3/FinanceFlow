-- Flag transactions over a threshold
SELECT *
FROM finance_db.etl.transactions
WHERE amount_usd > 5000
ORDER BY amount_usd DESC;
