import pytest
from final import BudgetPlanner
def test_budget_planner():
    """Test the BudgetPlanner class."""
    # Create a new budget for the month
    my_budget = BudgetPlanner("April")
    
    # Set total income
    my_budget.set_income(2000)
    
    # Add some expenses
    my_budget.add_expense("Rent", 300)
    my_budget.add_expense("Groceries", 150)
    my_budget.add_expense("Utilities", 180)
    
    # Check total expenses (300 + 150 + 180 = 630)
    assert my_budget.total_expenses() == 630
    
    # Check remaining budget (2000 - 630 = 1370)
    assert my_budget.remaining_budget() == 1370
    
    # Print the budget summary
    my_budget.print_summary()
