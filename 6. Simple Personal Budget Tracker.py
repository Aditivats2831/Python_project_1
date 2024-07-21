'''Simple Personal Budget Tracker
Description: A program to help users track their income and expenses, providing a summary of their financial status.'''

class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append((amount, description, 'income'))
        print(f"Income of ${amount} added. New balance: ${self.balance}")

    def add_expense(self, amount, description):
           self.balance -= amount
           self.transactions.append((amount, description, 'expense'))
           print(f"Expense of ${amount} added. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current Balance: ${self.balance}")

    def view_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            amount, description, type = transaction
            print(f"{type.capitalize()}: ${amount} - {description}")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter description: ")
            budget_tracker.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ")
            budget_tracker.add_expense(amount, description)
        elif choice == '3':
            budget_tracker.view_balance()
        elif choice == '4':
            budget_tracker.view_transactions()
        elif choice == '5':
            print("Exiting the budget tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
