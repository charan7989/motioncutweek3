# Import necessary libraries
import json
import os

# Expense Tracker Functions

def load_expenses(file_path):
    """Load expenses from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses, file_path):
    """Save expenses to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses, amount, category, description):
    """Add a new expense to the list."""
    expenses.append({"amount": amount, "category": category, "description": description})

def summarize_expenses(expenses):
    """Print a summary of expenses."""
    # Implement summary logic (e.g., total expenses, expenses by category)
    pass

def main():
    expenses_file = 'expenses.json'
    expenses = load_expenses(expenses_file)

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            add_expense(expenses, amount, category, description)
            save_expenses(expenses, expenses_file)
        elif choice == '2':
            summarize_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
