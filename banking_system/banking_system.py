# ---------------------------------
# Simple Banking System
# ---------------------------------

balance = 100000

print("===== BANKING SYSTEM =====")

while True:

    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter Choice: ")

    # Check Balance
    if choice == "1":

        print(f"\nYour Current Balance: ₹{balance}")

    # Deposit
    elif choice == "2":

        deposit = float(input("Enter Deposit Amount: ₹"))

        if deposit > 0:
            balance += deposit
            print(f"₹{deposit} Deposited Successfully")
        else:
            print("Invalid Amount")

    # Withdraw
    elif choice == "3":

        withdraw = float(input("Enter Withdraw Amount: ₹"))

        if withdraw <= balance:
            balance -= withdraw
            print(f"₹{withdraw} Withdrawn Successfully")

        else:
            print("Insufficient Balance")

    # Exit
    elif choice == "4":

        print("Thank You For Using Bank System")
        break

    else:
        print("Invalid Choice")
