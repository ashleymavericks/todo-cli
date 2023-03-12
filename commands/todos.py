import json
import os
from datetime import datetime
from rich.table import Table
from rich.console import Console

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
JSON_DIR = os.path.join(ROOT_DIR, 'database', 'lists')

console = Console()

# Deserialized data from todo list JSON file to Python object
def get_data(list_name):
    data = []
    if os.path.getsize(list_name) != 0:
        with open(list_name, 'r') as todo_list:
            data = json.load(todo_list)
    return data


# Update todo list JSON file with new_data serialized into JSON string
def update_data(list_name, new_data):
    with open(f'{JSON_DIR}/{list_name}', 'w') as todo_list:
        json.dump(new_data, todo_list, indent=True, sort_keys=True)


def add_item(args):
    list_name = args[0]
    data = get_data(f'{JSON_DIR}/{list_name}')
    data.append({
        'title': ' '.join(args[1:]),
        'completed': False,
        'created_at': datetime.now().strftime('%d-%b-%y %H:%M:%S')
    })
    update_data(list_name, data)
    console.print("Successfully added todo item!", style="bold green")


def show_items(args):
    list_name = args[0]
    data = get_data(f'{JSON_DIR}/{list_name}')
    if len(data) == 0:
        console.print(
            "No todo item in this list, try to add one!", style="bold red")

    completed = 0
    table = Table(title=list_name.replace('.json',''))
    table.add_column("Id")
    table.add_column("Task Name")
    table.add_column("Status")
    for index, todo_item in enumerate(data):
        if todo_item['completed'] == True:
            todo_status = '\u2714'
        else:
            todo_status = '\u2718'
        if todo_item['completed'] == True:
            completed += 1
        table.add_row(str(index + 1), todo_item['title'], todo_status)

    console.print(table)
    console.print(f"{completed}/{len(data)} todos completed!",
                  style="bold blue")


def edit_item(args):
    list_name = args[0]
    item_id = int(args[1])
    new_title = ' '.join(args[2:])
    data = get_data(f'{JSON_DIR}/{list_name}')
    for index, todo_item in enumerate(data):
        if item_id - 1 == index:
            if not new_title.strip():
                console.print(
                    "Sorry, can't keep a blank todo, try again!", style="bold yellow")
            else:
                todo_item['title'] = new_title
                update_data(list_name, data)
                console.print("Successfully edited the todo item!",
                              style="bold green")
            break
    else:
        console.print(
            'No todo found with this item_id, try again!', style="bold red")


def remove_item(args):
    list_name = args[0]
    item_id = int(args[1]) - 1
    data = get_data(f'{JSON_DIR}/{list_name}')
    if item_id < len(data):
        data.pop(item_id)
        update_data(list_name, data)
        console.print('Successfully removed todo item!', style="bold green")
    else:
        console.print(
            'No todo found with this item_id, try again!', style="bold red")


def mark_item_complete(args):
    list_name = args[0]
    item_id = int(args[1])
    data = get_data(f'{JSON_DIR}/{list_name}')
    for index, todo_item in enumerate(data):
        if item_id - 1 == index:
            if todo_item['completed'] == True:
                console.print('Todo is already completed!',
                              style="bold yellow")
            else:
                todo_item['completed'] = True
                update_data(list_name, data)
                console.print('Todo marked completed!',
                              style="bold green")
            break
    else:
        console.print(
            'No todo found with this item_id, try again!', style="bold red")


def mark_item_incomplete(args):
    list_name = args[0]
    item_id = int(args[1])
    data = get_data(f'{JSON_DIR}/{list_name}')
    for index, todo_item in enumerate(data):
        if item_id - 1 == index:
            if todo_item['completed'] == False:
                console.print('Todo is already incomplete!',
                              style="bold yellow")
            else:
                todo_item['completed'] = False
                update_data(list_name, data)
                console.print('Todo marked incomplete!', style="bold green")
            break
    else:
        console.print(
            'No todo found with this item_id, try again!', style="bold red")
