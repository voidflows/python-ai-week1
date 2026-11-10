# === TO-DO LIST MANAGER ===

# 1. Add task
# 2. View tasks
# 3. Mark task completed
# 4. Search tasks
# 5. Delete task
# 6. Exit

# Choose an option: 1

from todo_manager import TodoManager

manager = TodoManager()

while True:
    print("\n=========TO-DO LIST MANAGER=============")
    print("1.Add task ")
    print("2.View tasks ")
    print("3.Mark task completed ")
    print("4.Search task ")
    print("5.Delete task ")
    print("6.Exit")

    choice = int(input("Choose an option : "))
    if choice == 1:
        title = input("Enter title of the task : ")
        manager.add_task(title)
    elif choice == 2:
        manager.view_tasks()
    elif choice == 3:
        task_id = int(input("Enter task id : "))
        manager.mark_completed(task_id)
    elif choice == 4:
        keyword = input("Enter keyword : ")
        manager.search_tasks(keyword)
    elif choice == 5:
        task_id = int(input("Enter task id : "))
        manager.delete_task(task_id)
    elif choice == 6:
        print("Exit")
        break
    else:
        print("Invalid choice.")