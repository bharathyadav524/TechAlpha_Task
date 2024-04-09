# Function to add expense
def add_expense(expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    expenses.append({'category': category, 'amount': amount})
    print("Expense added successfully!")

# Function to generate insights
def generate_insights(expenses):
    categories = {}  # Dictionary to store total expenses for each category
    total_expense = 0

    for entry in expenses:
        category = entry['category']
        amount = entry['amount']
        total_expense += amount

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\nExpense Summary:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

    print("\nTotal Expense: ${:.2f}".format(total_expense))

# Main function
def main():
    expenses = []  # List to store expenses

    while True:
        print("\n1. Add Expense\n2. Generate Insights\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            if expenses:
                generate_insights(expenses)
            else:
                print("No expenses recorded yet.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
