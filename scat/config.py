import toml
from .filters import *
from dataclasses import dataclass
from typing import List

def load_filter(toml_file):
    config = toml.load(toml_file)
    filter_class = globals()[config.pop("class")]
    return filter_class(**config)

@dataclass
class Pipeline:

    steps : List[str]

    def __post_init__(self):
        self.filters = list(map(load_filter, self.steps))

    def apply(self, df):
        for filt in self.filters:
            df = df.map_partitions(filt)
        return df
