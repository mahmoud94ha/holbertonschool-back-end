#!/usr/bin/python3
"""api"""
import sys
import requests


def get_employee_todo_progress(employee_id):
    """func"""
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        employee_response.raise_for_status()
        todos_response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return

    employee_data = employee_response.json()
    todos_data = todos_response.json()

    employee_name = employee_data['name']
    completed_tasks = \
        [task['title'] for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    print(f"Employee {employee_name}\
          is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Employee ID not provided.")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
