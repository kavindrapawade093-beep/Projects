# ---------------------------------
# Student Management System
# ---------------------------------

students = {}

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")

        students[name] = marks

        print("Student Added Successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\nStudent Records:")

            for name, marks in students.items():
                print(f"Name: {name} | Marks: {marks}")

    # Search Student
    elif choice == "3":

        search_name = input("Enter Student Name: ")

        if search_name in students:
            print(f"{search_name} Marks:", students[search_name])

        else:
            print("Student Not Found")

    # Delete Student
    elif choice == "4":

        delete_name = input("Enter Student Name To Delete: ")

        if delete_name in students:
            del students[delete_name]
            print("Student Deleted Successfully")

        else:
            print("Student Not Found")

    # Exit
    elif choice == "5":

        print("System Closed")
        break

    else:
        print("Invalid Choice")
