from dataclasses import dataclass
import pandas as pd


@dataclass
class ComputeColumn:
    column_1: str
    column_2: str

    def __call__(self, df):
        df = df.assign(computed_col=(df[self.column_1] + df[self.column_2])) ** 2
        return df


@dataclass
class QueryFilter:
    query: str

    def __call__(self, df):
        return df.query(self.query)
