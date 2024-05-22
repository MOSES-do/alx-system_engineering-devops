#!/usr/bin/python3
"""REST API TO RETURN USER INFORMATION"""
import csv
import requests
import sys

if __name__ == "__main__":
    emp_todos = (
        f"https://jsonplaceholder.typicode.com/users/"
        f"{sys.argv[1]}/todos")
    emp_details = "https://jsonplaceholder.typicode.com/users/"

    user_row = []
    emp_name = requests.get(emp_details).json()
    for i in emp_name:
        if i['id'] == int(sys.argv[1]):
            EMPLOYEE_NAME = i['username']
            USER_ID = i['id']
    todos = requests.get(emp_todos).json()
    for item in todos:
        user_row.append(f'"{USER_ID}"')
        user_row.append(f',"{EMPLOYEE_NAME}"')
        user_row.append(f',"{item.get("completed")}"')
        user_row.append(f',"{item.get("title")}"')
        user_row.append('\n')

    with open(f'{sys.argv[1]}.csv', 'w') as csvfile:
        for row in user_row:
            csvfile.write(str(row))
    
