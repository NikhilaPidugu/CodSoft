def main():
    tasks = []
    while True:
        print("\n***To Do List*")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            n_tasks = int(input("How many tasks to be added: "))
            for _ in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
                
        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index+1}. {task['task']} - {status}")
                
        elif choice == '3':
            tindex = int(input("Enter the task number: "))-1
            if 0 <= tindex < len(tasks):
                del tasks[tindex]
                print("Task deleted!")
            else:
                print("Invalid task number")
                
        elif choice == '4':
            print("Exiting to-do list.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
