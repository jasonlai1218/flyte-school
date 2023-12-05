import pandas as pd
from flytekit import kwtypes, task, workflow
from flytekit.types.structured.structured_dataset import (
    StructuredDataset,
)
from typing_extensions import Annotated

all_cols = kwtypes(Name=str, Age=int, Height=int)
col = kwtypes(Age=int)


@task
def generate_pandas_df(a: int) -> pd.DataFrame:
    return pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [a, 22], "Height": [160, 178]})


@task
def get_subset_pandas_df(df: Annotated[StructuredDataset, all_cols]) -> Annotated[StructuredDataset, col]:
    df = df.open(pd.DataFrame).all()
    df = pd.concat([df, pd.DataFrame([[30]], columns=["Age"])])
    return StructuredDataset(dataframe=df)


@workflow
def simple_sd_wf(a: int = 19) -> Annotated[StructuredDataset, col]:
    pandas_df = generate_pandas_df(a=a)
    return get_subset_pandas_df(df=pandas_df)


if __name__ == "__main__":
    sd = simple_sd_wf()
