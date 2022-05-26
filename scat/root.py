import uproot3
import pandas as pd


def read_root_file(filename):
    with uproot3.open(filename) as f:
        df = pd.DataFrame(
            {k.decode("utf-8"): v.copy() for k, v in f["data"].arrays().items()}
        )
    # dask doesn't support multiindex
    # df.set_index(["seriesNumber", "eventNumber", "detNumber"])
    return df
