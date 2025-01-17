tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')
    print(tasks)

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed}" removed!')
    else:
        print("Invalid task number.")
        
while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task description: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        try:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")