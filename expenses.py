"""Keep the original storage imports working after moving to project.py."""

from project import format_expense, load_expenses, save_expenses

__all__ = ["format_expense", "load_expenses", "save_expenses"]
