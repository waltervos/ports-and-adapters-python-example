from pendulum import Date, date, now
from interest_calculator.app.ports.driven import (
    ForGettingTheCurrentDate,
    ForGettingTheInterestRate,
)


class FixedInterestRateRepository(ForGettingTheInterestRate):
    def __init__(self, rate: float) -> None:
        self._rate = rate

    def get_rate(self) -> float:
        return self._rate


class FixedCurrentDateRepository(ForGettingTheCurrentDate):
    def __init__(self, year: int, month: int, day: int) -> None:
        self._current_date = date(year=year, month=month, day=day)

    def get_current_date(self) -> Date:
        return self._current_date


class CurrentDateRepository(ForGettingTheCurrentDate):
    def get_current_date(self) -> Date:
        return now().date()
