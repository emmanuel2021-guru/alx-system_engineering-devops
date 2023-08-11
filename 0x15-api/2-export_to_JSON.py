#!/usr/bin/python3

"""This script uses a REST API for a given employee ID
and returns information about his/her TODO list progress"""

import csv
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
    filename = "{}.json".format(sys.argv[1])
    new_list = []
    for task in user_tasks:
        new_dict = {}
        new_dict.update({"task": task['title'],
                         "completed": task['completed'],
                         "username": user_info['username']})
        new_list.append(new_dict)
    data = {sys.argv[1]: new_list}
    with open(filename, "w", encoding="utf-8") as jsonFile:
        json.dump(data, jsonFile)
