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
    rows = []
    for task in user_tasks:
        row = []
        row.append('{}'.format(user_info['name']))
        row.append('{}'.format(user_info['username']))
        row.append('{}'.format(task['completed']))
        row.append('{}'.format(task['title']))
        rows.append(row)
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, 'w', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(rows)
