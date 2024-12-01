from pendulum import Date, Duration, date

from interest_calculator.app.ports.driven import ForGettingTheInterestRate, ForGettingTheCurrentDate
from interest_calculator.app.ports.driving import SimpleInterestCalculator


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

def test_zero_interest_rate_returns_zero():
    assert SimpleInterestCalculator(
        FixedInterestRateRepository(0.0), FixedCurrentDateRepository(2024, 12, 1)
    ).interest_from_now(100, Duration(months=1)) == 0.0


def test_less_than_one_month_returns_zero():
    assert SimpleInterestCalculator(
        FixedInterestRateRepository(0.1), FixedCurrentDateRepository(2024, 12, 1)
    ).interest_from_now(100, Duration(days=10)) == 0.0


def test_simple_interest_rate_is_easy():
    assert SimpleInterestCalculator(
        FixedInterestRateRepository(0.01), FixedCurrentDateRepository(2024, 12, 1)
    ).interest_from_now(100, Duration(months=12)) == 12.0


def test_full_months_are_counted():
    assert SimpleInterestCalculator(
        FixedInterestRateRepository(0.01), FixedCurrentDateRepository(2024, 12, 1)
    ).interest_from_now(100, Duration(days=55)) == 1.0