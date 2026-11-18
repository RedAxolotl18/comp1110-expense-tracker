"""Validate expense inputs for the COMP 1110 expense tracker."""


CATEGORIES = ("Food", "Transport", "School", "Other")


def parse_amount(text):
    """Return positive dollar input as whole cents, or raise ValueError."""
    whole, decimal_point, fraction = text.strip().partition(".")
    if not whole.isdecimal():
        raise ValueError("Enter a positive dollar amount, such as 4.50.")
    if decimal_point and (not fraction.isdecimal() or len(fraction) > 2):
        raise ValueError("Use one or two digits after the decimal point.")

    cents = int(whole) * 100
    if decimal_point:
        cents += int(fraction.ljust(2, "0"))
    if cents == 0:
        raise ValueError("The amount must be greater than zero.")
    return cents


def validate_category(text):
    """Return a standard category name, or raise ValueError."""
    choice = text.strip().lower()
    for category in CATEGORIES:
        if choice == category.lower():
            return category
    raise ValueError("Choose Food, Transport, School, or Other.")


def main():
    """Let the user try the expense amount and category checks."""
    print("Expense tracker input check")
    try:
        cents = parse_amount(input("Amount in dollars: "))
        category = validate_category(input("Category: "))
    except ValueError as error:
        print(f"Invalid expense: {error}")
        return

    dollars = cents // 100
    remainder = cents % 100
    print(f"Valid expense input: {category} - ${dollars}.{remainder:02d}")


if __name__ == "__main__":
    main()
