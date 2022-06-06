from abc import ABC, abstractmethod
from typing import List
import pandas as pd


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
    def __init__(self, after: str, before: str, column: str):
        self.after = after
        self.before = before
        self.column = column

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        after_start_date = data["Captured Time"] >= self.after
        before_end_date = data["Captured Time"] <= self.before
        between_two_dates = after_start_date & before_end_date
        
        return data.loc[between_two_dates]


class DistinctValuesFilter(AbstractFilter):
    def __init__(self, distinct_columns: List):
        self.distinct_columns = distinct_columns

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop_duplicates(subset=self.distinct_columns)

class EmptyCellsFilter(AbstractFilter):
    def __init__(self, columns: List):
        self.columns = columns

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna(subset=self.columns)

class ConvertToDateTimeFilter(AbstractFilter):
    def __init__(self, column: str, errors: str="raise"): # {‘ignore’, ‘raise’, ‘coerce’}
        self.column = column
        self.errors = errors

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        data[self.column] = pd.to_datetime(data[self.column], errors=self.errors)
        return data

class ConvertToDateFilter(AbstractFilter):
    def __init__(self, column: str, errors: str="raise"): # {‘ignore’, ‘raise’, ‘coerce’}
        self.column = column
        self.errors = errors

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        data[self.column] = pd.to_datetime(data[self.column], errors=self.errors).dt.date
        return data

class InRadiusFilter(AbstractFilter):
    def __init__(self, radius: int, power_plant_coordinates: (int, int)):
        self.radius = radius
        self.power_plant_coordinates = power_plant_coordinates

    def in_radius(self, latitude, longitude):
        return distance.distance(self.power_plant_coordinates, (latitude, longitude)).km < self.radius

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data[data.apply(lambda x: self.in_radius(x['Latitude'], x['Longitude']), axis=1)]
