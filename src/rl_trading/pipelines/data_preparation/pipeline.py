"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import set_dataframe_index, train_test_split, calculate_correlation

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=set_dataframe_index,
                inputs=['RAW_ICHI', 'params:index_name'],
                outputs="ichi",
                name="SET_INDEX",
            ),
        node(
                func=calculate_correlation,
                inputs=['ichi'],
                outputs="raw_correlation_matrix",
                name="COMPUT_RAW_DATA_CORRELATION",
            ),
        node(
                func=train_test_split,
                inputs=['ichi', 'params:input_params'],
                outputs=["train_df", "test_df"],
                name="SPILT_DATA",
            ),
        node(
                func=calculate_correlation,
                inputs=['train_df'],
                outputs="train_data_correlation_matrix",
                name="COMPUT_INPUT_CORRELATION",
            ),
    ])

