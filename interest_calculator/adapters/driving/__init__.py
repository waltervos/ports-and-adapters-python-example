import argparse
from pendulum import Duration
from interest_calculator.app.ports.driving import ForCalculatingInterest


class CliBasedInterestCalculator:
    def __init__(self, interest_calculator: ForCalculatingInterest) -> None:
        self._interest_calculator = interest_calculator

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "principal",
            help="Enter the principal on which to base your calculation",
            type=int,
        )
        parser.add_argument(
            "days",
            help="Enter the number of days from now on which you'd like to calculate your interest",
            type=int,
        )
        args = parser.parse_args()

        interest = self._interest_calculator.interest_from_now(
            args.principal, Duration(days=args.days)
        )
        print(f"The interest on {args.principal} after {args.days} days is {interest}")
