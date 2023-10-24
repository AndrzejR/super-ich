import os
import json

TODOS_FILEPATH = 'todos.txt'
DAILIES_FILEPATH = 'dailies.json'

if not os.path.exists(TODOS_FILEPATH):
    with open(TODOS_FILEPATH, 'w') as file:
        pass

if not os.path.exists(DAILIES_FILEPATH):
    with open(DAILIES_FILEPATH, 'w') as file:
        file.write('[]')
        pass


def read_todos():
    """
    Read the default file with todos
    and return the list of todos.
    :return: List of todos
    """
    with open(TODOS_FILEPATH, 'r') as todos_file:
        todos_from_file = [s.strip() for s in todos_file.readlines()]
    return todos_from_file


def write_todos(todos_to_write):
    """
    Write a list of todos to the default file.
    :param todos_to_write: List of todos to save
    :return: None
    """
    with open(TODOS_FILEPATH, 'w') as todos_file:
        todos_file.writelines(f"{s}\n" for s in todos_to_write)


def show_todos(todos_to_show):
    """
    Prints the todos one line per to-do.
    :param todos_to_show: List of todos to show
    :return: None
    """
    for i, t in enumerate(todos_to_show):
        row = f"{i + 1}: {t.strip()}"
        print(row)


def get_dailies():
    """
    Returns a list of dailies
    :return: List
    """
    with open(DAILIES_FILEPATH, 'r') as dailies_file:
        data = dailies_file.read()
        dailies = json.loads(data)
    return dailies


def write_dailies(dailies):
    """
    Saves the dailies in a json file
    :return: None
    """
    with open(DAILIES_FILEPATH, 'w') as dailies_file:
        dailies_file.write(json.dumps(dailies))
