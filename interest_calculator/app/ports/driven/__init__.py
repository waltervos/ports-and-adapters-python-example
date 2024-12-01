from abc import ABC, abstractmethod

from pendulum import Date


class ForGettingTheInterestRate(ABC):
    @abstractmethod
    def get_rate(self) -> float: ...


class ForGettingTheCurrentDate:
    @abstractmethod
    def get_current_date(self) -> Date: ...
