#!/usr/bin/python3
"""
gather employee data from API
"""

import requests


def fetch_employee_todo_list(employee_id):
    # API URL to fetch employee TODO list information
    url = (f"https://jsonplaceholder.typicode.com/"
           f"users/{employee_id}/todos")

    # Fetch data from the API
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        # Fetching employee name from the first todo item
        employee_name = data[0].get('username',
                                    'Unknown')
        total_tasks = len(data)
        completed_tasks = [task for task in data
                           if task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Display information
        print(f"Employee {employee_name} is "
              f"done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Failed to fetch TODO list for employee {employee_id}")


# Test the function with employee ID 2
fetch_employee_todo_list(2)
