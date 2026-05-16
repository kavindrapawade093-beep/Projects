# -----------------------------
# To-Do List App
# -----------------------------

tasks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Found")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Delete Task
    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks To Delete")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            delete_task = int(input("Enter Task Number To Delete: "))

            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print(f"{removed} Deleted Successfully")
            else:
                print("Invalid Task Number")

    # Exit
    elif choice == "4":
        print("App Closed")
        break

    else:
        print("Invalid Choice")
