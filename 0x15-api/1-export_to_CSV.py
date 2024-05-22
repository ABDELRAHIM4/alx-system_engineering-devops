#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import sys
import csv
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
    with open("{}.csv".format(emp), 'w') as f:
        form = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
        writer = csv.DictWriter(f, fieldnames=form)
        writer.writeheader()
        #print(writer)
        for task in todo_js:
            writer.writerow([emp, response.get("name"), task.get('completed'), task['title']])
            #writer.writerow({"USER_ID": "{}".format(str(emp)), "USERNAME" : "{}".format(str(response.get("name"))), "TASK_COMPLETED_STATUS" : "{}".format(str(task.get('completed'))), "TASK_TITLE" : str(task['title'])})
