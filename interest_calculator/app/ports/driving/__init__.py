from pendulum import Duration

from abc import ABC, abstractmethod

from pendulum import Duration


class ForCalculatingInterest(ABC):
    @abstractmethod
    def interest_from_now(self, principal: int, period: Duration) -> float: ...
