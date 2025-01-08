# ToDo List Application

This repository hosts a Python-based ToDo List application designed to help users efficiently manage their tasks through various functionalities such as adding, removing, viewing, saving, loading, and appending tasks.

## Features

- **Add Task**: Add new tasks with a category, description, and status.
- **Remove Task**: Remove tasks by their index.
- **View Tasks**: Display the list of tasks with their details.
- **Save Tasks**: Save all tasks to a file, overwriting the existing content.
- **Load Tasks**: Load and display tasks from a file.
- **Append Tasks**: Append only new tasks to the existing file without duplicating previously saved tasks.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shivamr021/todo-list.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-list
   ```
3. Ensure you have Python 3 installed on your system.

## Usage

1. Run the script:
   ```bash
   python todo_list.py
   ```
2. Follow the on-screen menu to manage your tasks.

## Menu Options

1. **Add a Task**: Input the category, description, and status of the task.
2. **Remove a Task**: Specify the index of the task to remove it.
3. **Tasks List**: View all tasks with their details.
4. **Save File**: Save all tasks to `task-list.txt`, overwriting any existing content.
5. **Load File**: Load and display tasks from `task-list.txt`.
6. **Append File**: Append only new tasks to `task-list.txt`.
7. **Exit**: Exit the application.

## Code Structure

- `addTask(category, task_desc, status)`: Adds a new task to the list.
- `removeTask(index)`: Removes a task by index.
- `showTasks()`: Returns the list of tasks.
- `saveFile()`: Saves all tasks to a file.
- `loadFile()`: Loads tasks from a file.
- `appendFile()`: Appends only new tasks to the file.
- `_writeTasksToFile(mode, tasks)`: Helper function to handle writing tasks to a file in the specified mode (overwrite or append).

## Enhancements

- **Task Duplication Prevention**: Implemented an `is_saved` flag to track tasks that have been saved, ensuring only new tasks are appended to the file.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```