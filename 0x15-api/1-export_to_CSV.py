#!/usr/bin/python3
"""REST API TO RETURN USER INFORMATION"""
import csv
import json
import requests
import sys
import urllib.request

if __name__ == "__main__":
    emp_todos = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{sys.argv[1]}/todos")
    emp_details = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{sys.argv[1]}")

    USER_ID = ""
    TASK_TITLE = []
    TASK_COMPLETED_STATUS = []
    USERNAME = ""
    user_dict = []
    user_row = {}
    with urllib.request.urlopen(emp_details) as res:
        emp = json.loads(res.read())
        USERNAME = emp.get("username")
        USER_ID = emp.get("id")
    todos = requests.get(emp_todos).json()
    for item in todos:
        """create an object of each element in the array"""
        user_row = (
            {"id": USER_ID, "uname": USERNAME, "title": item.get('completed'),
                "status": item.get('title')})
        """create a list of objects"""
        user_dict.append(user_row)

    with open('sys.argv[1].csv', 'w', newline='') as csvfile:
        fieldnames = user_dict[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        """write row headers
        writer.writeheader()"""
        """write row values"""
        writer.writerows(user_dict)
