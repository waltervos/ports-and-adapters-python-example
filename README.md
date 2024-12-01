# Ports & Adapters Python example
A simple example based on https://github.com/d-led/ports-and-adapters-archunit-example. I didn't create arch unit tests, I might do so later.

# Running the example
For easy use of this example, install uv (https://docs.astral.sh/uv/#getting-started). Then:

* To run the tests, use `uv run pytest`
* To run the CLI based adapter, use `uv run python -m interest_calculator <principal> <days>`
* To run the tests in watch mode, use `uv run ptw .`