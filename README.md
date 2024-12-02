# Ports & Adapters Python example
A simple example based on https://github.com/d-led/ports-and-adapters-archunit-example. I didn't create arch unit tests, which I might do later.

## Design
I chose to go full Enterprise Mode for this example and used Abstract Base Classes (ABC) for every port, including the driving ones. I might normally choose to use a concrete class without ABC for a driving port (but never for a driven port).

In terms of Ports & Adapters architecture (AKA Hexagonal Architecture), the `app` folder represents the hexagon. It defines two driven ports:
* `ForGettingTheCurrentDate`: Since calls to `date.now()` can be considered I/O as well, I decided to add this port. It's not present in d-led's example. It also makes the tests more explicit;
* `ForGettingTheInterestRate`: This port is used for retrieving the current interest rate. It can be implemented with a fixed rate (as I did in this example), but you can also imagine it might retrieve the interest rate from a database or web service.

There's also a driving port:
* `ForCalculatingInterest`: This is meant to be called with a principal and a time period (I've used Pendulum's duration here).

And there's also an implementation of the (driving) `ForCalculatingInterest` port: the `SimpleInterestCalculator` class. This implements the business logic, which is to get the interest rate, get the current date, determine the number of months contained in the period that was passed to it and then return the interest based on the principal.

The `adapters` folder then defines implementations for the driven ports:
* `FixedInterestRateRepository`: an implementation of `ForGettingTheInterestRate`, taking a fixed rate as a constructor argument;
* `FixedCurrentDateRepository`: an implementation of `ForGettingTheCurrentDate`, taking a fixed date as a constructor argument, which it simply returns when calling `get_current_date`. Created to be used in tests.
* `CurrentDateRepository`: This returns the actual current date. To be used "in production"

There's also a driving adapter in the `adapters` folder:
* `CliBasedInterestCalculator`: This uses the `ForCalculatingInterest` port, using input from command line arguments. Its constructor takes an instance of `ForCalculatingInterest` and is therefore not explicitly coupled to the `SimpleInterestCalculator` class.

The tests folder contains a couple of tests which check and demonstrate the core behaviour. I've only tested at the driving port, though with some imagination we could probably also test at the driving adapter level. The tests are not an adapter, they are an actor without an adapter (the CliBasedInterestCalculator is both an adapter and an actor).

Finally, in interest_calculator/__main__.py we find the configurator: It instantiates all driven adapters, then the `SimpleInterestCalculator`, and then the `CliBasedInterestCalculator` (driving adapter). It then calls the `run()` method on `CliBasedInterestCalculator`.


# Running the example
For easy use of this example, install uv (https://docs.astral.sh/uv/#getting-started). Then:

* To run the tests, use `uv run pytest`
* To run the CLI based adapter, use `uv run python -m interest_calculator <principal> <days>`
* To run the tests in watch mode, use `uv run ptw .`