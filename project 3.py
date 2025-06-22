import json
from datetime import datetime

DATA_FILE = 'expenses.json'

def load_expenses():
 try:
  with open(DATA_FILE, 'r') as file:
   return json.load(file)
 except (FileNotFoundError, json.JSONDecodeError):
  return []

def save_expenses(expenses):
 with open(DATA_FILE, 'w') as file:
  json.dump(expenses, file, indent=4)

def add_expense():
 amount = input("Enter amount spent: ")
 description = input("Enter description: ")
 category = input("Enter category (e.g., Food, Transport, Entertainment): ")

 try:
  amount = float(amount)
 except ValueError:
  print("Invalid amount. Please enter a number.")
  return

 date = datetime.now().strftime("%Y-%m-%d")
 expense = {
  'date': date,
  'amount': amount,
  'description': description,
  'category': category
 }

 expenses = load_expenses()
 expenses.append(expense)
 save_expenses(expenses)
 print("Expense added successfully!")

def view_expenses():
 expenses = load_expenses()
 if not expenses:
  print("No expenses recorded.")
  return

 print("\nAll Expenses:")
 for exp in expenses:
  print(f"Date: {exp['date']}, Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}")

def view_by_category():
 category = input("Enter category to filter by: ")
 expenses = load_expenses()
 filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]
 if not filtered:
  print(f"No expenses found for category '{category}'.")
  return

 print(f"\nExpenses in '{category}' category:")
 for exp in filtered:
  print(f"Date: {exp['date']}, Amount: {exp['amount']}, Description: {exp['description']}")

def monthly_summary():
 month = input("Enter month (YYYY-MM): ")
 expenses = load_expenses()
 monthly = [exp for exp in expenses if exp['date'].startswith(month)]
 if not monthly:
  print(f"No expenses found for month '{month}'.")
  return

 total = sum(exp['amount'] for exp in monthly)
 print(f"\nTotal expenses for {month}: {total}")
 print("Category-wise breakdown:")
 breakdown = {}
 for exp in monthly:
  cat = exp['category']
  breakdown[cat] = breakdown.get(cat, 0) + exp['amount']

 for cat, amt in breakdown.items():
  print(f"{cat}: {amt}")

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

if __name__ == "__main__":
 main()
