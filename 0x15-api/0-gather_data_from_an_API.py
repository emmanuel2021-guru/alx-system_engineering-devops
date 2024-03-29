#!/usr/bin/python3

"""This script uses a REST API for a given employee ID
and returns information about his/her TODO list progress"""

import json
import requests
import sys


if __name__ == "__main__":
    r_user_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(sys.argv[1]))
    r_user_info = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(sys.argv[1]))
    user_tasks = json.loads(r_user_tasks._content)
    user_info = json.loads(r_user_info._content)
    completed_tasks = 0
    for tasks in user_tasks:
        if tasks['completed'] is True:
            completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_info['name'],
                  completed_tasks, len(user_tasks)))
    for tasks in user_tasks:
        if tasks['completed'] is True:
            print("\t {}".format(tasks['title']))
