import json
from datetime import datetime

# File to store expense data
DATA_FILE = 'expenses.json'

# Function to load expenses from JSON file
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save expenses to JSON file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense():
    amount = input("Enter amount spent: ")
    description = input("Enter description: ")
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")

    # Validate amount
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Create expense record
    expense = {
        'date': date,
        'amount': amount,
        'description': description,
        'category': category
    }

    # Load existing expenses, add new one, and save
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAll Expenses:")
    for exp in expenses:
        print(f"Date: {exp['date']}, Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}")

# Function to view expenses by category
def view_by_category():
    category = input("Enter category to filter by: ")
    expenses = load_expenses()

    filtered_expenses = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    if not filtered_expenses:
        print(f"No expenses found for category '{category}'.")
        return

    print(f"\nExpenses in '{category}' category:")
    for exp in filtered_expenses:
        print(f"Date: {exp['date']}, Amount: {exp['amount']}, Description: {exp['description']}")

# Function to view monthly expense summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    expenses = load_expenses()

    # Filter expenses by month
    monthly_expenses = [exp for exp in expenses if exp['date'].startswith(month)]
    if not monthly_expenses:
        print(f"No expenses found for month '{month}'.")
        return

    total = sum(exp['amount'] for exp in monthly_expenses)
    print(f"\nTotal expenses for {month}: {total}")
    print("Category-wise breakdown:")

    # Calculate total per category
    category_totals = {}
    for exp in monthly_expenses:
        category = exp['category']
        category_totals[category] = category_totals.get(category, 0) + exp['amount']

    for category, total in category_totals.items():
        print(f"{category}: {total}")

# Main menu
def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
