#!/usr/bin/python3
"""api"""
from requests import get
from sys import argv


if __name__ == '__main__':
    """main"""

    id = argv[1]
    task = []
    done = 0
    total = 0
    endpoint = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = get(endpoint).json()
    name = user.get('name')
    todos = "https://jsonplaceholder.typicode.com/todos/"
    endpoint2 = get(todos).json()
    for item in endpoint2:
        if item.get('userId') == int(id):
            if item.get('completed') is True:
                task.append(item['title'])
                done += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for item in task:
        print("\t {}".format(item))
