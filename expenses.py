import csv
import os

def load_expenses(filename="expenses.csv"):
    """
    Read CSV records; handle missing files and malformed data.
    Returns a list of expense dictionaries or objects.
    """
    expenses = []
    if not os.path.exists(filename):
        # Handle missing file by returning an empty list
        return expenses
    
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Validate and parse essential fields to ensure no malformed data crashes the app
                    description = row["description"]
                    category = row["category"]
                    amount_cents = int(row["amount_cents"])
                    expenses.append({
                        "description": description,
                        "category": category,
                        "amount_cents": amount_cents
                    })
                except (KeyError, ValueError):
                    # Skip malformed rows gracefully
                    continue
    except Exception:
        # Catch other potential file-reading errors
        pass
        
    return expenses

def save_expenses(expenses, filename="expenses.csv"):
    """
    Save the current expense records to CSV.
    """
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["description", "category", "amount_cents"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense)
    except Exception as e:
        print(f"Error saving expenses: {e}")

def format_expense(expense):
    """
    Return a readable expense line with its amount in dollars.
    Amounts are stored in cents, so we divide by 100 to display as dollars.
    """
    dollars = expense["amount_cents"] / 100.0
    return f"[{expense['category']}] {expense['description']} - ${dollars:.2f}"
