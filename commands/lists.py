import os
import json
from datetime import datetime
from rich.table import Table
from rich.console import Console

console = Console()

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
JSON_DIR = os.path.join(ROOT_DIR, 'database', 'lists')
JSON_FILE = os.path.join(ROOT_DIR, 'database', 'lists.json')


def get_lists_data(list_name):
    data = {}
    with open(list_name, 'r') as master_list:
        if os.path.getsize(list_name) != 0:
            data = json.load(master_list)
    return data


def show_lists(args):
    data = get_lists_data(JSON_FILE)
    if data:
        table = Table(title="Todo Lists")
        table.add_column("List Name")
        table.add_column("Todo Count")
        for key in data.keys():
            file_name = data[key]['file_name']
            with open(f'{JSON_DIR}/{file_name}', 'r') as todo_list:
                todo_count = len(json.load(todo_list))
            table.add_row(key, str(todo_count))
        console.print(table)
    else:
        console.print("No lists to show, kindly first create one!", style="bold yellow")


def use_list(args):
    if args:
        list_name = args[0]
        data = get_lists_data(JSON_FILE)
        if data:
            if data.get(list_name):
                console.print(
                    " Successfully selected the given list!", style="bold green")
                return data[list_name]['file_name']
            else:
                console.print("Not a valid list name, try again!",
                              style=" bold red")
        else:
            print("No lists to choose from, kindly first create one!",
                  style="bold yellow")
    else:
        console.print(
            "Provide a valid list name to use, try again!", style=" bold yellow")


def create_list(args):
    if args:
        list_name = args[0]
        data = get_lists_data(JSON_FILE)
        if data.get(list_name):
            console.print(
                "List already exists, try a different name!", style="bold yellow")
        else:
            new_list = {
                "file_name": f'{list_name}.json',
                "created_at": datetime.now().strftime('%d-%b-%y %H:%M:%S')
            }

            data[list_name] = new_list

            with open(f'{JSON_DIR}/{list_name}.json', 'w') as new_list:
                new_list.write('[\n]')
                console.print("Successfully created the new list",
                              style="bold green")

            # add the newly created list to lists.json
            with open(JSON_FILE, 'w') as master_list:
                json.dump(data, master_list, indent=True, sort_keys=True)
    else:
        console.print(
            "Provide a valid list name to create, try again!", style=" bold yellow")


def drop_list(args):
    data = get_lists_data(JSON_FILE)
    if args:
        list_name = args[0]
        if data.get(list_name):
            removed_list = data.pop(list_name)
            file_name = removed_list['file_name']
            os.remove(f'{JSON_DIR}/{file_name}')
            
            with open(JSON_FILE, 'w') as master_list:
                json.dump(data, master_list, indent=True, sort_keys=True)
                
            console.print("List is successfully dropped", style="bold green")
            
            return file_name
        else:
            console.print("Not a valid list name, try again!",
                          style=" bold red")
    else:
        console.print(
            "Provide a valid list name to create, try again!", style=" bold yellow")
