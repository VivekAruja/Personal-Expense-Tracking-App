from expense import Expense
import calendar
import datetime
from typing import List

# Main function that runs the Expense Tracker
def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for a new expense
    expense = get_user_expense()

    # Save the new expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Summarize expenses from the file and compare with the budget
    summarize_expenses(expense_file_path, budget)

# Function to get user input for an expense
def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")  # Ask for expense name
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))  # Ask for expense amount
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")  # Handle invalid amount input

    # Define expense categories
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    # Ask the user to select a category for the expense
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")  # Display category options

        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                # Create an Expense object with user input
                new_expense = Expense(
                    name=expense_name, category=selected_category, amount=expense_amount
                )
                return new_expense
            else:
                print("Invalid category. Please try again!")  # Handle invalid category selection
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-numeric input

# Function to save an expense to a file
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")  # Write expense data to file

# Function to read expenses from a file and summarize them
def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expenses: List[Expense] = []
    try:
        with open(expense_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                expense_name, expense_amount, expense_category = line.strip().split(",")
                line_expense = Expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category,
                )
                expenses.append(line_expense)
    except FileNotFoundError:
        print(f"No expenses file found at {expense_file_path}.")
        return

    # Summarize expenses by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")  # Display total amount per category

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")  # Display total expenses

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")  # Display remaining budget

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))  # Display daily budget

# Function to color the text green (for display purposes)
def green(text):
    return f"\033[92m{text}\033[0m"

# Run the main function if this file is executed
if __name__ == "__main__":
    main()
