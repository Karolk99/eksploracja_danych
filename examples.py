from eksploracja_danych.large_data_fitler import LargeDataFilter
from chunk_filters import (
    DistinctValuesFilter,
    DateFilter,
    SpecificValuesInRowFilter,
    DropColumnsFilter,
)
from visualize_localization import VisualizeLocalizations


# Filter columns
columns_to_drop = [
    "Location Name",
    "MD5Sum",
    "Surface",
    "Radiation",
    "Uploaded Time",
    "Loader ID",
]
chunk_filter = DropColumnsFilter(columns_to_drop)
LargeDataFilter().filter_data(
    "only_cpm_locations.csv",
    "filtered_columns.csv",
    chunk_filter,
)

# Distinct devices
distinct_columns = ["Device ID"]
chunk_filter = DistinctValuesFilter(distinct_columns)
LargeDataFilter().filter_distinct(
    "filtered_columns.csv",
    "locations_dist.csv",
    chunk_filter,
)

# Draw locations
VisualizeLocalizations.visualize("locations_dist.csv")
