expenses = []  # Each expense will be stored as a dictionary

def add_expense():
    """Add a new expense with item, category, and amount."""
    item = input("Enter item name: ").strip()
    category = input("Enter category (Food, Transport, Bills, etc.): ").strip()
    try:
        amount = float(input("Enter amount ($): "))
        expenses.append({"item": item, "category": category, "amount": amount})
        print(f"Added {item} (${amount:.2f}) under {category}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    """Display all expenses and total cost."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Expense List ---")
    total = 0
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['item']} ({e['category']}): ${e['amount']:.2f}")
        total += e['amount']
    print(f"\nTotal Spent: ${total:.2f}")

def clear_expenses():
    """Clear all saved expenses."""
    confirm = input("Are you sure you want to clear all expenses? (y/n): ").lower()
    if confirm == "y":
        expenses.clear()
        print("All expenses cleared.")
    else:
        print("Action canceled.")

def main_menu():
    """Main interactive loop for the Expense Tracker."""
    while True:
        print("\n==== Expense Tracker Menu ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Clear All Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            clear_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

# Run the program
if __name__ == "__main__":
    main_menu()