#!/usr/bin/python3
"""
For a given employee ID, returns information about
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder."
                        "typicode.com/users/{}".format(user_id))

    if user.status_code != 200:
        print("User not found.")
        sys.exit(1)

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.'
                         'typicode.com/todos')
    total_tasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(user_id):
            total_tasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks'
          '({}/{}):'.format(name, completed, total_tasks))

    print('\n'.join(["\t" + task.get('title') for task in todos.json()
                     if task.get('userId') == int(user_id) and
                     task.get('completed')]))
