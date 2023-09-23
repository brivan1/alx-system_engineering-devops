#!/usr/bin/python3
"""
Function that exports data into a flatfile in
the JSON format
"""

if __name__ == "__main__":
    import json
    import requests as req
    import sys

    employeeID = sys.argv[1]
    user = req.get("https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todos = req.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(employeeID):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[employeeID] = taskList

    fn = employeeID + '.json'
    with open(fn, mode='w') as f:
        json.dump(todoUser, f)
