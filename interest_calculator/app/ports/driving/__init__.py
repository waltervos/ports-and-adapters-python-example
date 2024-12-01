from pendulum import Duration
from interest_calculator.app.ports.driven import (
    ForGettingTheCurrentDate,
    ForGettingTheInterestRate,
)

from abc import ABC, abstractmethod

from pendulum import Duration


class ForCalculatingInterest(ABC):
    @abstractmethod
    def interest_from_now(self, principal: int, period: Duration) -> float: ...


class SimpleInterestCalculator(ForCalculatingInterest):
    def __init__(
        self,
        interest_rate_repo: ForGettingTheInterestRate,
        current_date_repo: ForGettingTheCurrentDate,
    ) -> None:
        self._interest_rate_repo = interest_rate_repo
        self._current_date_repo = current_date_repo

    def interest_from_now(self, principal: int, period: Duration) -> float:
        current_date = self._current_date_repo.get_current_date()
        end_date = current_date + period
        months = current_date.diff(end_date).in_months()

        return self._interest_rate_repo.get_rate() * months * principal
