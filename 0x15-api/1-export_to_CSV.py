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

    user_dict = []
    emp_name = requests.get(emp_details).json()
    for i in emp_name:
        if i['id'] == int(sys.argv[1]):
            EMPLOYEE_NAME = i['username']
            USER_ID = i['id']
    todos = requests.get(emp_todos).json()
    for item in todos:
        """create an object of each element in the array"""
        user_row = (
            {"id": USER_ID, "uname": EMPLOYEE_NAME,
                "title": item.get("completed"), "status": item.get("title")})
        """create a list of objects"""
        user_dict.append(user_row)

    with open('f"{sys.argv}".csv', 'w') as csvfile:
        fieldnames = user_dict[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        """write row headers
        writer.writeheader()"""
        """write row values"""
        writer.writerows(user_dict)
