#!/usr/bin/python3
"""REST API TO RETURN USER INFORMATION"""
import requests
import urllib.request
import json
import sys


if __name__ == "__main__":
    emp_todos = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos/"
    emp_details = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    tasks = []
    tasks_title = []
    completed_tasks = 0
    emp_name = ""

    with urllib.request.urlopen(emp_details) as res:
        emp = json.loads(res.read())
        emp_name = emp.get("name")

    todos = requests.get(emp_todos).json()
    for item in todos:
        done_task = item.get("completed")
        if done_task is True:
            completed_tasks += 1
        title = item.get("title")
        tasks_title.append(title)
        for key in item.items():
            if key == "completed":
                tasks.append(key)

    len_of_total_tasks = len(tasks)

    print(
        f"Employee {emp_name} is done with tasks "
        f"({completed_tasks}/{len_of_total_tasks}):")
    [print(f"\t{title}") for title in tasks_title]
