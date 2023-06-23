#!/usr/bin/python3
"""api"""
from json import dump
from requests import get

if __name__ == '__main__':
    """main"""
    endpoint = 'https://jsonplaceholder.typicode.com'
    user = get('{}/users'.format(endpoint)).json()
    target = get('{}/todos'.format(endpoint)).json()
    list = {}
    for i in user:
        list[i['id']] = []
        for x in target:
            fmt = {'username': i['username'], 'task': x['title'],
                   'completed': x['completed']}
            if x['userId'] == i['id']:
                list[i['id']].append(fmt)
    json = 'todo_all_employees.json'
    with open(json, 'w') as result:
        dump(list, result)
