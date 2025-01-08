import datetime

class ToDoList:
    def __init__(self):
        self.task_list = []

    def addTask(self, category, task_desc, status):
        self.task_list.append({
            "Added": datetime.datetime.now(),
            "Category": category,
            "Task Description": task_desc,
            "Status": status,
            "is_saved": False 
        })
        return True

    def removeTask(self, index):
        if 0 <= index < len(self.task_list):
            self.task_list.pop(index)
            return True
        return False

    def showTasks(self):
        return self.task_list

    def _writeTasksToFile(self, mode, tasks):
        with open("task-list.txt", mode) as file:
            for task in tasks:
                file.write(f"Added on - {task['Added']}\n")
                file.write(f"Category - {task['Category']}\n")
                file.write(f"Description - {task['Task Description']}\n")
                file.write(f"Status - {task['Status']}\n")
                file.write("\n") 

    def saveFile(self):
        self._writeTasksToFile("w", self.task_list)
        for task in self.task_list:
            task['is_saved'] = True

    def appendFile(self):
        new_tasks = [task for task in self.task_list if not task['is_saved']]
        self._writeTasksToFile("a", new_tasks)
        for task in new_tasks:
            task['is_saved'] = True

    def loadFile(self):
        with open("task-list.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())


task = ToDoList()

exit_program = False
while not exit_program:
    print("MENU: ")
    print("""
        1. Add a task
        2. Remove a task
        3. Tasks list
        4. Save File
        5. Load File
        6. Append File
        7. Exit """)
    choice = input("Choose an option: ")

    match choice:

        case "1":
            category = input("Category: ")
            task_desc = input("Task description: ")
            status = input("Status: ")
            if task.addTask(category, task_desc, status):
                print("Task added successfully")
            else:
                print("Task add failed!")

        case "2":
            index = int(input("Enter the index of task you want to remove: "))
            if task.removeTask(index):
                print("Task removed successfully")
            else:
                print("Task remove failed!")

        case "3":
            for i, tasks in enumerate(task.showTasks()): 
                print(f"Added on - {tasks['Added']}") 
                print(f"Category - {tasks['Category']}") 
                print(f"Description - {tasks['Task Description']}")
                print(f"Status - {tasks['Status']}")

        case "4":
            task.saveFile()
            print("File saved successfully") 

        case "5":
            task.loadFile()

        case "6":
            task.appendFile()
            print("File appended successfully")

        case "7":
            exit_program = True

        case _:
            print("Invalid choice! Please try again.")
