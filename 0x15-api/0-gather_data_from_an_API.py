#!/usr/bin/python3
"""REST API TO RETURN USER INFORMATION"""
import json
import requests
import urllib.request
import sys


if __name__ == "__main__":
    emp_todos = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{sys.argv[1]}/todos/")
    emp_details = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{sys.argv[1]}")

    tasks = []
    TASKS_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    EMPLOYEE_NAME = ""

    with urllib.request.urlopen(emp_details) as res:
        emp = json.loads(res.read())
        EMPLOYEE_NAME = emp.get("name")

    todos = requests.get(emp_todos).json()
    for item in todos:
        done_task = item.get("completed")
        if done_task is True:
            NUMBER_OF_DONE_TASKS += 1
            TASKS_TITLE.append(item.get("title"))
        for k in item:
            if k == "completed":
                tasks.append(k)

    TOTAL_NUMBER_OF_TASKS = len(tasks)

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks"
        f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    [print(f"\t {title}") for title in TASKS_TITLE]
