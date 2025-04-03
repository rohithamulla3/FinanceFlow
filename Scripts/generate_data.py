import pandas as pd
import numpy as np
from utils.logger import get_logger

logger = get_logger("DataGenerator")

def generate_synthetic_data():
    logger.info("Generating synthetic financial transaction data...")
    df = pd.DataFrame({
        'transaction_id': np.arange(1000, 1100),
        'amount': np.random.uniform(10, 5000, 100),
        'currency': np.random.choice(['USD', 'EUR', 'GBP'], 100),
        'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='H')
    })
    df.to_csv('/tmp/generated_transactions.csv', index=False)
    logger.info("Data saved to /tmp/generated_transactions.csv")
