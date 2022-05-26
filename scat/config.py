import toml
from .filters import *


def load_filter(toml_file):
    config = toml.load(toml_file)
    filter_class = globals()[config.pop("class")]
    return filter_class(**config)
