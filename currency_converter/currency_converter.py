# ---------------------------------
# Currency Converter
# ---------------------------------

print("===== CURRENCY CONVERTER =====")

# Exchange Rates
usd_rate = 83.0
eur_rate = 90.0

while True:

    print("\n1. INR to USD")
    print("2. INR to EUR")
    print("3. USD to INR")
    print("4. EUR to INR")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # INR to USD
    if choice == "1":

        inr = float(input("Enter Amount in INR: ₹"))

        usd = inr / usd_rate

        print(f"USD: ${usd:.2f}")

    # INR to EUR
    elif choice == "2":

        inr = float(input("Enter Amount in INR: ₹"))

        eur = inr / eur_rate

        print(f"EUR: €{eur:.2f}")

    # USD to INR
    elif choice == "3":

        usd = float(input("Enter Amount in USD: $"))

        inr = usd * usd_rate

        print(f"INR: ₹{inr:.2f}")

    # EUR to INR
    elif choice == "4":

        eur = float(input("Enter Amount in EUR: €"))

        inr = eur * eur_rate

        print(f"INR: ₹{inr:.2f}")

    # Exit
    elif choice == "5":

        print("Currency Converter Closed")
        break

    else:
        print("Invalid Choice")
