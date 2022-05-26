import dask.array as da


def dask_memory_usage_GB(dask_object):
    return dask_object.memory_usage(deep=True).compute().sum() / 1024**3


def dask_histogram(dask_dataframe, column, bins, bins_range):
    h, bins = da.histogram(
        dask_dataframe[column].to_dask_array(), bins=bins, range=bins_range
    )
    histogram = h.compute()
    centroids = bins[:-1] + (bins[1] - bins[0]) / 2
    return centroids, histogram
