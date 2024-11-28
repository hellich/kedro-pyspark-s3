"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import when


def preprocess_companies(companies: DataFrame) -> DataFrame:
    return companies.withColumn(
        "iata_approved", when(companies.iata_approved == "t", True).otherwise(False)
    )
