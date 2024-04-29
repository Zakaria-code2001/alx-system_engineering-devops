#!/usr/bin/python3
"""
gather employee data from API
"""

import requests


def fetch_employee_todo_list(employee_id):
    # API URL to fetch employee TODO list information
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Fetch data from the API
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        user_data = response.json()
        employee_name = user_data.get('name', 'Unknown')
    else:
        print(f"Failed to fetch user data for employee {employee_id}")
        return

    # Fetch employee's todo list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)

    # Check if todo request was successful
    if todo_response.status_code == 200:
        todos = todo_response.json()
        completed_tasks = [task for task in todos if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)

        # Display information
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Failed to fetch TODO list for employee {employee_id}")


# Test the function with employee ID 2
fetch_employee_todo_list(2)
