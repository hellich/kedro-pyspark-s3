"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
from pyspark.sql import DataFrame

def preprocess_companies(companies: DataFrame) -> DataFrame:
    ...