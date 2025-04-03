import pandas as pd
import numpy as np
from utils.logger import get_logger

logger = get_logger("LambdaTransform")

def lambda_transform():
    logger.info("Transforming data in Lambda simulation...")
    df = pd.read_csv('/tmp/generated_transactions.csv')
    df['amount_usd'] = df['amount'] * np.random.uniform(0.9, 1.1, len(df))  # Simulate FX
    df.to_csv('/tmp/transformed_transactions.csv', index=False)
    logger.info("Transformed data saved to /tmp/transformed_transactions.csv")
