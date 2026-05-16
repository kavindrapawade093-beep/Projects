# ---------------------------------
# Expense Tracker Project
# ---------------------------------

expenses = []

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    # Add Expense
    if choice == "1":

        item = input("Enter Expense Name: ")
        amount = float(input("Enter Amount: "))

        expenses.append({
            "item": item,
            "amount": amount
        })

        print("Expense Added Successfully!")

    # View Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No Expenses Found")

        else:
            print("\nYour Expenses:")

            for expense in expenses:
                print(
                    f"Item: {expense['item']} | "
                    f"Amount: ₹{expense['amount']}"
                )

    # Show Total
    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\nTotal Expense: ₹{total}")

    # Exit
    elif choice == "4":

        print("Expense Tracker Closed")
        break

    else:
        print("Invalid Choice")
