#!/usr/bin/python3
"""
gather employee data from API
"""

import re
import requests
import sys


def fetch_employee_todo_list(employee_id):
    # API URL to fetch employee TODO list information
    url = (f"https://jsonplaceholder.typicode.com/todos/"
           f"{employee_id}")

    # Fetch data from the API
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        employee_name = data.get('name', 'Unknown')
        total_tasks = len(data)
        completed_tasks = [task for task in data if
                           task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Display information
        print(f"Employee {employee_name} is done with"
              f" tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Failed to fetch TODO list"
              f" for employee {employee_id}")


fetch_employee_todo_list(1)
