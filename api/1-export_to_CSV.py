#!/usr/bin/python3
"""api"""
from csv import writer, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":
    """main"""
    id = argv[1]
    endpoint = "https://jsonplaceholder.typicode.com"
    user = get("{}/users/{}".format(endpoint, id)).json()
    target = get("{}/users/{}/todos".format(endpoint, id)).json()
    username = user.get('username')
    file_format = '{}.csv'.format(id)
    with open(file_format, 'w') as result:
        for data in target:
            data = [data['userId'], username, data['completed'], data['title']]
            fmt = writer(result, quoting=QUOTE_ALL)
            fmt.writerow(data)
