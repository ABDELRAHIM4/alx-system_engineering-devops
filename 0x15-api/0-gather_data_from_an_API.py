#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import sys
import requests
if __name__ == "__main__":
    emp = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    res = requests.get(url + "users/{}".format(emp))
    response = res.json()
    params = {"userId" : emp}
    todo = requests.get(url + "todos", params=params)
    todo_js = todo.json()
    com = []
    for task in todo_js:
        if task.get('completed') is  True:
            com.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(response.get("name"), len(com), len(todo_js)))
    for task in todo_js:
        if task.get('completed') is  True:
            print("  {}".format(task.get('title')))
