from typing import List
import pandas as pd
from chunk_filters import AbstractFilter


class LargeDataFilter:
    memory_available: int = 1000000000

    def filter_data(
        self,
        input_file: str,
        output_file: str,
        filter: AbstractFilter,
    ) -> None:
        csv_iterator = self._create_csv_iterator(input_file)

        first_iteration = True
        for chunk in csv_iterator:
            filter.filter(chunk).to_csv(
                output_file, mode="a", header=first_iteration, index=False
            )
            first_iteration = False if first_iteration else first_iteration

    def filter_distinct(
        self,
        input_file: str,
        output_file: str,
        filter: AbstractFilter,
    ) -> None:
        csv_iterator = self._create_csv_iterator(input_file)

        df = pd.concat([filter.filter(chunk) for chunk in csv_iterator])
        df = filter.filter(df)

        df.to_csv(output_file, mode="a", header=True, index=False)

    def _create_csv_iterator(self, input_file):
        chunk_size = self._calculate_chunk_size(input_file)

        return pd.read_csv(
            input_file,
            iterator=True,
            chunksize=int(chunk_size),
        )

    def _calculate_chunk_size(self, input_file):
        nrows = 10
        df_sample = pd.read_csv(
            input_file,
            nrows=nrows,
        )

        df_sample_size = df_sample.memory_usage(index=True).sum()
        return (self.memory_available / df_sample_size) / nrows
