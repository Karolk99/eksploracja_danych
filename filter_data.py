from typing import List
import pandas as pd

class FilterData:
    @staticmethod
    def filter_data(
        input_file: str,
        output_file: str,
        columns_to_drop: List[str],
        filter_function,  # (pd.DataFrame, List[int]) -> DataFrame:
        memory_available: int = 1000000000,
    ) -> None:
        nrows = 10
        df_sample = pd.read_csv(
            input_file,
            nrows=nrows,
        )

        df_sample_size = df_sample.memory_usage(index=True).sum()
        chunk_size = (memory_available / df_sample_size) / nrows

        csv_iterator = pd.read_csv(
            input_file,
            iterator=True,
            chunksize=int(chunk_size),
        )

        first_iteration = True
        for chunk in csv_iterator:
            filter_function(chunk, columns_to_drop).to_csv(
                output_file, mode="a", header=first_iteration, index=False
            )
            first_iteration = False if first_iteration else first_iteration

    @staticmethod
    def fileter_distinct(
        input_file: str,
        output_file: str,
        distinct_columns: List[str],
        memory_available: int = 1000000000,
    ) -> pd.DataFrame:
        nrows = 10
        df_sample = pd.read_csv(
            input_file,
            nrows=nrows,
        )

        df_sample_size = df_sample.memory_usage(index=True).sum()
        chunk_size = (memory_available / df_sample_size) / nrows

        csv_iterator = pd.read_csv(
            input_file,
            iterator=True,
            chunksize=int(chunk_size),
        )

        df = pd.concat(
            [chunk.drop_duplicates(subset=distinct_columns) for chunk in csv_iterator]
        )

        df.drop_duplicates(subset=distinct_columns, inplace=True)

        df.to_csv(output_file, mode="a", header=True, index=False)

    @staticmethod
    def filter_function(
        chunk: pd.DataFrame, columns_to_drops: List[str]
    ) -> pd.DataFrame:
        return chunk.drop(
            columns=columns_to_drops,
        )

    @staticmethod
    def filter_cpm_rows(
        input_file: str,
        memory_available: int = 1000000000,
    ):
        # df = pd.read_csv("only_cpm_locations.csv")
        # device_ids = df["Device ID"].to_list()

        nrows = 10
        df_sample = pd.read_csv(
            input_file,
            nrows=nrows,
        )

        df_sample_size = df_sample.memory_usage(index=True).sum()
        chunk_size = (memory_available / df_sample_size) / nrows

        csv_iterator = pd.read_csv(
            input_file,
            iterator=True,
            chunksize=int(chunk_size),
        )

        first_iteration = True
        for chunk in csv_iterator:
            chunk = chunk[chunk["Unit"] == "cpm"]
            chunk.to_csv(
                "filtered_data_cpm.csv", mode="a", header=first_iteration, index=False
            )
            first_iteration = False if first_iteration else first_iteration

    @staticmethod
    def filter_by_date(
        input_file: str,
        memory_available: int = 1000000000,
    ):
        nrows = 10
        df_sample = pd.read_csv(
            input_file,
            nrows=nrows,
        )

        df_sample_size = df_sample.memory_usage(index=True).sum()
        chunk_size = (memory_available / df_sample_size) / nrows

        csv_iterator = pd.read_csv(
            input_file,
            iterator=True,
            chunksize=int(chunk_size),
        )

if __name__ == "__main__":
    # FilterData.fileter_distinct(
    #     "measurements-out.csv",
    #     "locations_distinct.csv",
    #     ["Device ID"],
    # )
    FilterData.filter_data(
        "filtered_data_cpm.csv",
        "2xfiltered_data_cpm.csv",
        [
            "Unit",
            "Height",
            "Location Name",
            "Device ID",
        ],
        FilterData.filter_function,
    )

# ['Captured Time', 'Latitude', 'Longitude', 'Value', 'Unit',
#       'Location Name', 'Device ID', 'MD5Sum', 'Height', 'Surface',
#       'Radiation', 'Uploaded Time', 'Loader ID']
