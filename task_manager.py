import logging
import json
import os
import pandas as pd  # Ensure you have pandas imported
import streamlit as st

# Configure logging to track events and errors
logging.basicConfig(filename='task_manager.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dummy login credentials for testing
DUMMY_EMAIL = "testuser@example.com"
DUMMY_PASSWORD = "password123"

# Define Task Structure
class Task:
    task_id_counter = 1  # Class attribute to track task IDs globally

    def __init__(self, title):
        self.id = Task.task_id_counter  # Assign the next available task ID
        self.title = title  # Task title provided by the user
        self.completed = False  # By default, a new task is not completed
        Task.task_id_counter += 1  # Increment the task ID counter for the next task

# Task Management Functions
class TaskManager:
    def __init__(self):
        self.tasks = []  # List that will store Task objects

    def add_task(self, title):
        # Check if a task with the same title already exists
        if any(task.title.lower() == title.lower() for task in self.tasks):
            return False  # Task already exists
        
        task = Task(title)  # Create a new Task object
        self.tasks.append(task)  # Add the new task to the list
        logging.info(f'Task added: {task.title} (ID: {task.id})')  # Log the addition
        return True  # Task successfully added

    def view_tasks(self):
        return self.tasks  # Return the list of tasks

    def delete_task(self, task_id):
        # Iterate through tasks to find and remove the specified task by ID
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)  # Remove the task from the list
                logging.info(f'Task deleted: {task.title} (ID: {task.id})')  # Log the deletion
                return True  # Task successfully deleted
        return False  # Task not found

    def mark_task_complete(self, task_id):
        # Iterate through tasks to find the specified task by ID and mark it as complete
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True  # Mark the task as completed
                logging.info(f'Task marked as complete: {task.title} (ID: {task.id})')  # Log the update
                return True  # Task successfully marked
        return False  # Task not found

    def save_tasks(self):
        # Save the current list of tasks to a JSON file
        try:
            with open('tasks.json', 'w') as file:
                json_tasks = [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in self.tasks]
                json.dump(json_tasks, file)  # Write tasks to the file
            logging.info("Tasks saved to tasks.json.")  # Log successful save
        except Exception as e:
            logging.error(f'Error saving tasks: {e}')  # Log any errors encountered

    def load_tasks(self):
        # Load tasks from the JSON file if it exists
        if not os.path.exists('tasks.json'):
            open('tasks.json', 'w').close()  # Create an empty file if it doesn't exist
            logging.info("tasks.json file created.")  # Log file creation
            return
        
        try:
            with open('tasks.json', 'r') as file:
                json_tasks = json.load(file)  # Load tasks from the file
                self.tasks = [Task(task['title']) for task in json_tasks]  # Create Task objects from loaded data
                for i, task in enumerate(self.tasks):
                    task.id = json_tasks[i]['id']  # Set task ID
                    task.completed = json_tasks[i]['completed']  # Set task completion status
                Task.task_id_counter = max([task.id for task in self.tasks], default=0) + 1  # Update task ID counter
            logging.info("Tasks loaded from tasks.json.")  # Log successful load
        except json.JSONDecodeError:
            logging.warning("tasks.json is empty, starting with an empty task list.")  # Handle empty JSON file
        except Exception as e:
            logging.error(f'Error loading tasks: {e}')  # Log any errors encountered

# Streamlit Login Functionality
def login():
    # Get user email and password input from sidebar
    email = st.sidebar.text_input("Email", "")
    password = st.sidebar.text_input("Password", "", type="password")
    
    # Check login credentials on button press
    if st.sidebar.button("Login"):
        if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
            st.session_state.logged_in = True  # Set session state to logged in
            st.success("Login successful.")  # Show success message
        else:
            st.error("Invalid credentials.")  # Show error message for invalid login

# Streamlit UI
def main():
    # Initialize session state for login status if not already set
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    login()  # Call login function

    if st.session_state.logged_in:
        task_manager = TaskManager()  # Initialize task manager
        task_manager.load_tasks()  # Load existing tasks (if any)

        st.title("Task Manager CLI Application")  # Set the title for the Streamlit app

        # Add Task
        title = st.text_input("Task Title")  # Input field for task title
        if st.button("Add Task"):  # Button to add task
            if title.strip() == "":  # Check if title is empty
                st.error("Please provide the title name to add.")  # Error message for empty title
            elif task_manager.add_task(title):  # Check if task can be added
                st.success(f"Task '{title}' added successfully.")  # Success message
                task_manager.save_tasks()  # Save tasks after adding
            else:
                st.error(f"Error: A task with the title '{title}' already exists.")  # Error message for duplicate task

        # View Tasks
        if st.button("View Tasks"):  # Button to view tasks
            tasks = task_manager.view_tasks()  # Get the list of tasks
            if tasks:
                # Prepare task data for display with ID, Title, and Status
                task_data = [(task.id, task.title, "Completed" if task.completed else "Pending") for task in tasks]
                # Display the data as a table with headers
                st.table(pd.DataFrame(task_data, columns=["ID", "Name", "Status"]))  # Display tasks in a structured format
            else:
                st.info("No tasks available.")  # Info message for no tasks

        # Mark Task as Complete
        task_id_to_complete = st.number_input("Enter Task ID to Mark as Complete", min_value=1, step=1)  # Input for task ID to complete
        if st.button("Mark Task as Complete"):  # Button to mark task as complete
            if task_manager.mark_task_complete(task_id_to_complete):
                st.success(f"Task with ID '{task_id_to_complete}' marked as complete successfully.")  # Success message
                task_manager.save_tasks()  # Save tasks after marking
            else:
                st.error("Task not found. Please check the ID and try again.")  # Error message for task not found

        # Delete Task
        task_id_to_delete = st.number_input("Enter Task ID to Delete", min_value=1, step=1)  # Input for task ID to delete
        if st.button("Delete Task"):  # Button to delete task
            if task_manager.delete_task(task_id_to_delete):
                st.success(f"Task with ID '{task_id_to_delete}' deleted successfully.")  # Success message
                task_manager.save_tasks()  # Save tasks after deletion
                task_manager.load_tasks()  # Reload tasks after deletion
            else:
                st.error("Task not found. Please check the ID and try again.")  # Error message for task not found

        # Save Tasks
        if st.button("Save Tasks"):  # Button to save tasks
            task_manager.save_tasks()  # Save tasks to file
            st.success("Tasks saved.")  # Success message
            st.session_state.download_available = True  # Flag for download availability

        # Download Tasks as JSON (show only once)
        if 'download_available' in st.session_state and st.session_state.download_available:
            with open('tasks.json', 'r') as file:
                json_data = file.read()  # Read the tasks data
            st.download_button("Download tasks.json", json_data, file_name='tasks.json', mime='application/json')  # Button to download JSON file

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()  # Start the Streamlit application
