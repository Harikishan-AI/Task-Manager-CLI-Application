# Task Manager CLI Application

### Description
The **Task Manager CLI Application** is a Python-based command-line tool for managing tasks efficiently. This application allows users to add, view, delete, and mark tasks as complete. All tasks are saved locally to a JSON file (`tasks.json`), making them persistent across multiple sessions. Additionally, tasks are displayed in a neat tabular format to improve readability, and logging functionality is provided to track actions and handle errors effectively.

### Features
- **Add Tasks**: Add new tasks while ensuring unique titles (case-insensitive).
- **View Tasks**: View all tasks in a table format (ID, Title, Status).
- **Delete Tasks**: Remove tasks based on their unique task ID.
- **Complete Tasks**: Mark tasks as completed and avoid re-marking already completed tasks.
- **Persistent Storage**: Automatically saves tasks to a JSON file (`tasks.json`), ensuring data is retained between sessions.
- **Logging**: Logs important events such as task addition, deletion, and errors into a log file (`task_manager.log`).

## Technologies Used
- **Python**: Programming language used for development.
- **Streamlit**: A framework for creating web applications.
- **JSON**: Format for saving tasks.
- **Pandas**: For handling and displaying data in table format.

## Prerequisites
Before running the application, ensure you have the following installed on your system:
- Python 3.7 or higher
- pip (Python package installer)


Clone the project repository from GitHub using the following command:
```bash
git clone https://github.com/harikishan-task-manager/task-manager-cli.git
```

Install the required packages:
```bash
pip install streamlit pandas
```

Navigate to the project directory:
```bash
cd path/to/task-manager
```

Start the Streamlit application:
```bash
streamlit run task_manager.py
```
Open your web browser and go to http://localhost:8501 to access the Task Manager interface.

## Usage
- Login: Enter the dummy credentials (email: testuser@example.com, password: password123) to access the app.

## Adding Tasks:
- Enter a task title in the "Task Title" input field and click "Add Task."
- If the title is empty, an error message will prompt you to provide a valid title.

## Viewing Tasks:
Click on "View Tasks" to display all tasks in a table format.

## Marking Tasks as Complete:
- Enter the Task ID you want to mark as complete and click "Mark Task as Complete."

## Deleting Tasks:
- Enter the Task ID you want to delete and click "Delete Task."

## Saving Tasks:
- Click on "Save Tasks" to save the current task list to a JSON file.

## Downloading Tasks:
- A button will appear to download the task list as a JSON file.

## File Structure
task-manager-cli/
│
├── task_manager.py         # Main Python script for the Task Manager CLI
├── tasks.json              # JSON file to store tasks (created automatically)
├── task_manager.log        # Log file for tracking actions and errors
├── README.md               # Documentation for the project
└── requirements.txt        # Optional: Dependencies for the project
