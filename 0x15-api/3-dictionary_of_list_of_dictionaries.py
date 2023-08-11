#!/usr/bin/python3

"""This script uses a REST API for a given employee ID
and returns information about his/her TODO list progress"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    r_all_user_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos')
    all_user_tasks = json.loads(r_all_user_tasks._content)
    id_list = []
    for task in all_user_tasks:
        if task['userId'] not in id_list:
            id_list.append(task['userId'])
    print(id_list)
    filename = "todo_all_employees.json"
    all_user_tasks_dict = {}
    for user_id in id_list:
        r_user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id))
        user_tasks = json.loads(r_user_tasks._content)
        r_user_info = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'
                .format(user_id))
        user_info = json.loads(r_user_info._content)
        new_list = []
        for task in user_tasks:
            new_dict = {}
            new_dict.update({"task": task['title'],
                             "completed": task['completed'],
                             "username": user_info['username']})
            new_list.append(new_dict)
        data = {user_id: new_list}
        all_user_tasks_dict.update(data)
    with open(filename, "w", encoding="utf-8") as jsonFile:
        json.dump(all_user_tasks_dict, jsonFile)
