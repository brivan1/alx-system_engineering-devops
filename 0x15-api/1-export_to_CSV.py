#!/usr/bin/python3

""" script exports data from an API to a flat file in csv format """

if __name__ == "__main__":

    import csv
    import requests as req
    import sys

    employeeID = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    user = req.get("{}/{}".format(url, str(employeeID)))
    name = user.json().get('username')
    todos = req.get('{}/{}/todos'.format(url,str(employeeID)))
    tasks = todos.json()
    fn = '{}.csv'.format(str(employeeID))

    with open(fn, mode='w')as f:
        for task in tasks:
            f.write('"{}", "{}", "{}", "{}"\n'
                    .format(employeeID, name, task.get('completed'),
                        task.get('title')))
