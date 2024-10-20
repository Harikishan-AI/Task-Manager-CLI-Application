# Task Manager CLI Application

#### App link: https://task-manager-cli-app.streamlit.app/  (use Email ID: testuser@example.com, Password: password123)

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
git clone https://github.com/Harikishan-AI/Task-Manager-CLI-Application.git
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
```bash
task-manager-cli/
│
├── task_manager.py         # Main Python script for the Task Manager CLI
├── tasks.json              # JSON file to store tasks (created automatically)
├── task_manager.log        # Log file for tracking actions and errors
├── README.md               # Documentation for the project
└── requirements.txt        # Optional: Dependencies for the project
```

## Output:

![{BFAACECA-386C-402A-BEFD-4BCC2F8B0EDA}](https://github.com/user-attachments/assets/a6668f17-73cd-46c4-9322-7471952f0b05)

![{EB67222B-64B5-4620-B9B0-78CAE2003830}](https://github.com/user-attachments/assets/4e856239-80b1-4636-a08a-b8bd268f9694)

![{8845E225-9A47-46ED-B24C-5AED3956D13E}](https://github.com/user-attachments/assets/1b646582-29a6-4aac-98b0-a6102158909f)

