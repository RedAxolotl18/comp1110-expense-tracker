"""Check Fares's expense input validation."""

import pytest

from project import parse_amount, validate_category


def test_parse_amount():
    """Check exact cents, whitespace, small amounts, and invalid input."""
    valid_amounts = {
        "4": 400,
        "4.5": 450,
        "4.50": 450,
        " 4.50 ": 450,
        "0.01": 1,
        "0.10": 10,
        "0.29": 29,
        "0004.50": 450,
        "90071992547409.93": 9007199254740993,
    }
    for text, expected in valid_amounts.items():
        assert parse_amount(text) == expected

    invalid_amounts = [
        "", " ", "0", "0.00", "-1", "+1", "abc", "4.", ".50",
        "1.001", "4.500", "1.2.3", "NaN", "Infinity", "1e2", "$4",
        "1,000", "4 .50", "4. 50",
    ]
    for text in invalid_amounts:
        with pytest.raises(ValueError):
            parse_amount(text)


def test_validate_category():
    """Check every category, normalized input, and rejected choices."""
    for category in ("Food", "Transport", "School", "Other"):
        assert validate_category(category) == category
        assert validate_category(category.upper()) == category
        assert validate_category(" " + category.lower() + " ") == category

    for text in ("", " ", "Shopping", "Foods", "1", "Food Transport"):
        with pytest.raises(ValueError):
            validate_category(text)
