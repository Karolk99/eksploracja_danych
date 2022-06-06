from large_data_fitler import LargeDataFilter
from chunk_filters import (
    DropColumnsFilter,
    SpecificValuesInRowFilter,
    EmptyCellsFilter,
    ConvertToDateFilter,
)


def clean_data(input_file, output_file):
    tmp_file = "temporary.csv"
    tmp_file2 = "temporary2.csv"
    tmp_file3 = "temporary3.csv"
    tmp_file4 = "temporary4.csv"

    filter = SpecificValuesInRowFilter("Unit", ["cpm"])
    LargeDataFilter().filter_data(
        input_file,
        tmp_file,
        filter,
    )

    columns_to_drop = [
        "Unit",
        "Location Name",
        "MD5Sum",
        "Surface",
        "Radiation",
        "Uploaded Time",
        "Loader ID",
    ]
    filter = DropColumnsFilter(columns_to_drop)
    LargeDataFilter().filter_data(
        tmp_file,
        tmp_file2,
        filter,
    )

    columns = ["Captured Time", "Latitude", "Longitude", "Value"]
    filter = EmptyCellsFilter(columns)
    LargeDataFilter().filter_data(
        tmp_file2,
        tmp_file3,
        filter,
    )

    filter = ConvertToDateFilter("Captured Time", errors="coerce")
    LargeDataFilter().filter_data(
        tmp_file3,
        tmp_file4,
        filter
    )

    columns = ["Captured Time"]
    filter = EmptyCellsFilter(columns)
    LargeDataFilter().filter_data(
        tmp_file4,
        output_file,
        filter,
    )

# clean_data("data/measurements-out.csv", "data/cleaned_data.csv")
