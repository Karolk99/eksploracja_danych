from abc import ABC, abstractclassmethod, abstractmethod

from typing import List
import pandas as pd

class AbstractFilter(ABC):
    
    @abstractmethod
    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

class DropColumnsFilter(AbstractFilter):
    def init(self, columns_to_drop: List[str]):
        self.columns_to_drop = columns_to_drop
    
    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop(
            columns=self.columns_to_drops,
        )

class SpecificValuesInRowFilter(AbstractFilter):
    def init(self, column: str, acceptable_values: List):
        self.column = column
        self.acceptable_values = acceptable_values
    
    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data[data[self.column].isin(self.acceptable_values)]

class DateFilter(AbstractFilter):
    def init(self, after: pd.Timestamp, before: pd.Timestamp, column: str):
        self.after = after
        self.before = self.before
        self.column = column
    
    def filter(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.loc[self.before:self.after]
