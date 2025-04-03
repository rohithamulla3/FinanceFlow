from great_expectations.dataset import PandasDataset
import pandas as pd
from utils.logger import get_logger

logger = get_logger("DataValidation")

def validate_data():
    logger.info("Validating data with Great Expectations...")
    df = pd.read_csv('/tmp/generated_transactions.csv')
    dataset = PandasDataset(df)
    assert dataset.expect_column_values_to_not_be_null('transaction_id').success
    assert dataset.expect_column_values_to_be_between('amount', min_value=1, max_value=10000).success
    logger.info("Data validation passed.")
