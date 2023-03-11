<div align="center">
<h1 align="center">Todo CLI</h1>
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"/><br><br>
A simple to-do list application that can be accessed via a Command-Line Interface (CLI), application allow users to add, remove, edit, and list tasks in a convenient and efficient manner.<br><br>
</div>

---

## Features

- Create a todo list
- Show all the todo lists
- Add, edit, delete, mark as complete, incomplete etc the todo items present in those lists
- Show all the todo items in a particular items

## Commands to use the CLI app

prefixes for the commands: `list`, `todo`

- `list show` -> show all the todo lists
- `list create list_name` -> create a list with list_name
- `todo add todo_title` -> add a todo item in the selected list
- `todo all` -> show all todos in the selected list
- `todo edit item_id new_title` -> edit the todo item with id=item_id
- `todo remove item_id` -> remove the todo item with id=item_id
- `todo complete item_id` -> mark a todo item with id=item_id as complete
- `todo incomplete item_id` -> mark a todo item with id=item_id as incomplete
- `help` -> print all the commands provided by the app
- `quit` -> exit the application

## JSON schema

- Schema for storing all the todo lists

```JSON
{
  "list1": {
    "file_name": "list1.json",
    "created_at": "timestamp"
  }
}
```
- Schema for storing todo's in a todo list
```JSON
[
  {
    "title": "todo_title1",
    "completed": false,
    "created_at": "timestamp"
  },
  {
    "title": "todo_title2",
    "completed": true,
    "created_at": "timestamp"
  }
]
```