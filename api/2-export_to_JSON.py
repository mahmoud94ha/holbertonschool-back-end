#!/usr/bin/python3
"""api"""
from requests import get
from sys import argv
from json import dump

if __name__ == "__main__":
    """main"""
    id = argv[1]
    endpoint = "https://jsonplaceholder.typicode.com"
    user = get("{}/users/{}".format(endpoint, id)).json()
    target = get('{}/todos?userId={}'.format(endpoint, id)).json()
    username = user.get('username')
    list = {}
    list[id] = []
    for i in target:
        appends = {'task': i['title'], 'completed': i['completed'],
                   'username': username}
        list[id].append(appends)
    file_format = '{}.json'.format(id)
    with open(file_format, 'w') as result:
        dump(list, result)
