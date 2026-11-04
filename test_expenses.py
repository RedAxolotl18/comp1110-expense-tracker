import os
from expenses import load_expenses, save_expenses, format_expense

def test_format_expense():
    expense = {"description": "Coffee", "category": "Food", "amount_cents": 450}
    assert format_expense(expense) == "[Food] Coffee - $4.50"

def test_load_missing_file():
    # Should return an empty list if the file does not exist
    loaded = load_expenses(filename="non_existent_expenses.csv")
    assert loaded == []

def test_save_and_load_expenses():
    test_filename = "temp_test_expenses.csv"
    sample_expenses = [
        {"description": "Bus ticket", "category": "Transport", "amount_cents": 275}
    ]
    
    # Test saving
    save_expenses(sample_expenses, filename=test_filename)
    assert os.path.exists(test_filename)
    
    # Test loading back
    loaded_expenses = load_expenses(filename=test_filename)
    assert len(loaded_expenses) == 1
    assert loaded_expenses[0]["description"] == "Bus ticket"
    assert loaded_expenses[0]["amount_cents"] == 275
    
    # Cleanup test file
    if os.path.exists(test_filename):
        os.remove(test_filename)
