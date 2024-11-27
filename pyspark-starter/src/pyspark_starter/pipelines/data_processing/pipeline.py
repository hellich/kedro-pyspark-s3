"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import preprocess_companies


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_companies,
            inputs="companies",
            outputs="preprocessed_companies",
            name="preprocess_companies_node"
        )
    ])
