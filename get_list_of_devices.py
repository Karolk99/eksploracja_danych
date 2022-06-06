from large_data_fitler import LargeDataFilter
from chunk_filters import DistinctValuesFilter

def get_list_of_devices(input_file, output_file):
    filter = DistinctValuesFilter(["Device ID"])
    LargeDataFilter().filter_distinct(
        input_file,
        output_file,
        filter,
    )


if __name__ == "__main__":
    get_list_of_devices('data/clean_data.csv', 'data/devices_list2.csv')