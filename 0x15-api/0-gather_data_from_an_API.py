#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import sys
import requests
if __name__ == "__main__":
    emp = int(sys.argv[1])
    url = f'https://jsonplaceholder.typicode.com/users/{emp}'
    res = requests.get(url)
    response = res.json()
    url1 = f'https://jsonplaceholder.typicode.com/todos/{emp}'
    todo = requests.get(url1)
    todo_js = todo.json()
    com = []
    for task in todo_js:
        if todo_js.get('completed') is  True:
            com.append(todo_js.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(response.get("name"), len(com), len(todo_js)))
    for task in todo_js:
        if todo_js.get('completed') is  True:
            print(todo_js.get('title'))
