#!/usr/bin/python3

""" script displays a TODO list for a given employee with an ID """

import requests as req
import sys

if __name__ == '__main__':

    employeeID = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com"
    url = baseUrl + "/" + employeeID

    response = req.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = req.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

            print("Employee {} is done with tasks({}/{}):"
                    .format(employeeName, done, len(tasks)))

            for task in done_tasks:
                print("\t {}".format(task.get('title')))
