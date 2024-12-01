from interest_calculator.adapters.driven import (
    CurrentDateRepository,
    FixedInterestRateRepository,
)
from interest_calculator.adapters.driving import CliBasedInterestCalculator
from interest_calculator.app.ports.driving import SimpleInterestCalculator


def main():
    interest_calculator = SimpleInterestCalculator(
        FixedInterestRateRepository(0.1), CurrentDateRepository()
    )

    cli = CliBasedInterestCalculator(interest_calculator=interest_calculator)

    cli.run()


if __name__ == "__main__":
    main()
