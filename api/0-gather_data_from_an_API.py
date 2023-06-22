#!/usr/bin/python3
"""api"""
from requests import get
from sys import argv

if __name__ == "__main__":
    """main"""
    id = argv[1]
    endpoint = 'https://jsonplaceholder.typicode.com'
    user = get(f"{endpoint}/users/{id}").json()
    getreq = get(f"{endpoint}/users/{id}/todos").json()
    username = user.get('name')
    counter = 0
    for i in getreq:
        if i['completed']:
            counter += 1
    print(f"Employee {username} is done with tasks({counter}/{len(getreq)}):")
    for msg in getreq:
        if msg.get('completed'):
            print(f"\t {msg.get('title')}")
