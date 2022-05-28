from abc import ABC, abstractmethod

from typing import List
import pandas as pd
from geopy import distance


class AbstractFilter(ABC):
    @abstractmethod
    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


class DropColumnsFilter(AbstractFilter):
    def __init__(self, columns_to_drop: List[str]):
        self.columns_to_drop = columns_to_drop

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop(
            columns=self.columns_to_drop,
        )


class SpecificValuesInRowFilter(AbstractFilter):
    def __init__(self, column: str, acceptable_values: List):
        self.column = column
        self.acceptable_values = acceptable_values

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data[data[self.column].isin(self.acceptable_values)]


class DateFilter(AbstractFilter):
    def __init__(self, after: pd.Timestamp, before: pd.Timestamp, column: str):
        self.after = after
        self.before = self.before
        self.column = column

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.loc[self.before: self.after]


class DistinctValuesFilter(AbstractFilter):
    def __init__(self, distinct_columns: List):
        self.distinct_columns = distinct_columns

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop_duplicates(subset=self.distinct_columns)


class InRadiusFilter(AbstractFilter):
    def __init__(self, radius: int, power_plant_coordinates: (int, int)):
        self.radius = radius
        self.power_plant_coordinates = power_plant_coordinates

    def in_radius(self, latitude, longitude):
        return distance.distance(self.power_plant_coordinates, (latitude, longitude)).km < self.radius

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data[data.apply(lambda x: self.in_radius(x['Latitude'], x['Longitude']), axis=1)]
