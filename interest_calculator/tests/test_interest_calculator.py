from pendulum import Duration, date

from interest_calculator.adapters.driven import (
    FixedCurrentDateRepository,
    FixedInterestRateRepository,
)
from interest_calculator.app.simple import SimpleInterestCalculator


def test_zero_interest_rate_returns_zero():
    assert (
        SimpleInterestCalculator(
            FixedInterestRateRepository(0.0), FixedCurrentDateRepository(2024, 12, 1)
        ).interest_from_now(100, Duration(months=1))
        == 0.0
    )


def test_less_than_one_month_returns_zero():
    assert (
        SimpleInterestCalculator(
            FixedInterestRateRepository(0.1), FixedCurrentDateRepository(2024, 12, 1)
        ).interest_from_now(100, Duration(days=10))
        == 0.0
    )


def test_simple_interest_rate_is_easy():
    assert (
        SimpleInterestCalculator(
            FixedInterestRateRepository(0.01), FixedCurrentDateRepository(2024, 12, 1)
        ).interest_from_now(100, Duration(months=12))
        == 12.0
    )


def test_full_months_are_counted():
    assert (
        SimpleInterestCalculator(
            FixedInterestRateRepository(0.01), FixedCurrentDateRepository(2024, 12, 1)
        ).interest_from_now(100, Duration(days=55))
        == 1.0
    )
