#!/usr/bin/python3
"""create a dicionary list of dictionaries"""
import json
import requests

if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    response = response.json()

    dict_row = {}

    for key in response:
        var_list = []
        id = key["id"]
        purl = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        response_purl = requests.get(purl)
        response_purl = response_purl.json()
        for j in response_purl:
            user = {}
            user["username"] = key["username"]
            user['task'] = j['title']
            user['completed'] = j['completed']
            var_list.append(user)
        dict_row[id] = var_list

    with open("todo_all_employees.json", 'w') as path:
        json.dump(dict_row, path)
