-- Create transaction table with additional fields
CREATE OR REPLACE TABLE finance_db.etl.transactions (
    transaction_id NUMBER PRIMARY KEY,
    user_id NUMBER,
    merchant_id NUMBER,
    transaction_type STRING,
    amount FLOAT,
    currency STRING,
    amount_usd FLOAT,
    location STRING,
    timestamp TIMESTAMP,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
