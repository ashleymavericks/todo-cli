import json, os
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname('todos.py'), '..'))
                           
JSON_DIR = os.path.join(ROOT_DIR, 'storage', 'work.json')      

def get_data(list_name):
    data = []
    if os.path.getsize(list_name) != 0:
        with open(list_name, 'r') as todo_list:
            data = json.load(todo_list)
    return data

def add_item(args):
    today_date = str(datetime.today())
    data = get_data(JSON_DIR)
    data.append({
        'title': ' '.join(args),
        'completed': False,
        'created_at': today_date
    })
    with open(JSON_DIR, 'w') as todo_list:
        data = json.dump(data, todo_list, indent=True, sort_keys=True)

def show_items(args):
    data = get_data(JSON_DIR)
    for todo in data:
        print(todo['title'])
    
