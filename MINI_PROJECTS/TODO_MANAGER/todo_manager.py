import json
from pathlib import Path

class TodoManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.file_path = Path(__file__).resolve().parent / "tasks.json"

        # Path(__file__).resolve().parent identifies the folder containing todo_manager.py.
        # / "tasks.json" represents the JSON file inside that folder.
        # .exists() checks whether the file already exists.
        # If the file doesn't exist, self.save_tasks() creates it.

        if self.file_path.exists():
            self.load_tasks()
        else:
            self.save_tasks()

    def add_task(self,title):
        new_task = {
            "id" : self.next_id,
            "title" : title,
            "completed" : False
        }
        self.tasks.append(new_task)
        self.next_id += 1
        self.save_tasks()
        print("Task added Successfully!!!")
        print(self.tasks)

    def view_tasks(self):
        # if len(self.tasks) == 0:
        #     print("No Tasks available.")

        # Step 1: Check whether self.tasks is empty
        if not self.tasks:
            print("No Tasks available.")  # Step 2: If empty, print "No tasks available"
            return
        print("\n========YOUR TASKS===========")

        for task in self.tasks: # Step 3: Otherwise, loop through self.tasks
            status = "Completed" if task['completed'] else "Pending"

            # Step 4: Print each task's ID, title and completion status
            print(
            f"ID: {task['id']} | "
            f"Title: {task['title']} | "
            f"Status: {status}"
        )

    print("================================")

    def mark_completed(self, task_id):
        for task in self.tasks: # Loop through the list of dictionaries
            if task['id'] == task_id: #if the user input task id is present in the list of dictionary then mark it as completed and return.

                if task['completed']:
                    print("Task is already completed.")
                    return

                task['completed'] = True
                self.save_tasks()
                print("Task completed successfully!")
                return
        print("No matching task ID found.")

    def search_tasks_by_id(self,task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                status = "Completed" if task['completed'] else "Pending"
                print(f"ID: {task['id']} | " f"Title: {task['title']} | " f"Status: {status}")
                return
            
        print("No tasks found with the given id.")

    def search_tasks(self, keyword):
        found = False

        for task in self.tasks:
            if keyword.lower() in task["title"].lower():
                status = "Completed" if task['completed'] else "Pending"
                print(f"ID: {task['id']} | " f"Title: {task['title']} | " f"Status: {status}")
                found = True
        if not found:
            print("No tasks found!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:  # Check whether task ID matches
                self.tasks.remove(task) # Remove the dictionary from self.tasks
                self.save_tasks()
                print("Task deleted successfully!") # Print success message
                return # Return
        print("Task not found") #If no matching task exists

    def save_tasks(self):
        data = {
            "next_id" :self.next_id,
            "tasks" : self.tasks
        }

        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump(data,file,indent=4)
            # file = The opened file where the JSON will be written
            # indent = 4 -->> Formats JSON using 4 spaces for each indentation level

    def load_tasks(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.tasks = data["tasks"]
        self.next_id = data["next_id"]




        
