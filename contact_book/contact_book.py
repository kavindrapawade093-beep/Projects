# ---------------------------------
# Contact Book Project
# ---------------------------------

contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Contact
    if choice == "1":

        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")

        contacts[name] = number

        print("Contact Added Successfully!")

    # View Contacts
    elif choice == "2":

        if len(contacts) == 0:
            print("No Contacts Found")

        else:
            print("\nSaved Contacts:")

            for name, number in contacts.items():
                print(f"Name: {name} | Phone: {number}")

    # Search Contact
    elif choice == "3":

        search_name = input("Enter Name To Search: ")

        if search_name in contacts:
            print(
                f"{search_name} Phone Number:",
                contacts[search_name]
            )

        else:
            print("Contact Not Found")

    # Delete Contact
    elif choice == "4":

        delete_name = input("Enter Name To Delete: ")

        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact Deleted Successfully!")

        else:
            print("Contact Not Found")

    # Exit
    elif choice == "5":

        print("Contact Book Closed")
        break

    else:
        print("Invalid Choice")
