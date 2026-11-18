# comp1110-expense-tracker
A Python expense tracker for our COMP 1110 group project.

## Current progress

Fares's amount and category checks are ready. Dollar input is stored as
integer cents, and categories are standardized to Food, Transport, School,
or Other. Invalid input produces an error message.

Areej's loading, saving, and formatting functions are in expenses.py, with
their existing tests in test_expenses.py. The full menu, remaining project
functions, and final integration are upcoming work.

## Run the input checks

```text
python project.py
```

## Run all current tests

```text
python -m pip install -r requirements.txt
python -m pytest
```
