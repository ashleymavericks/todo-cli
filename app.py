from commands import commands_dict
from rich.table import Table
from rich.console import Console

console = Console()

def parse(command):
    cmd_list = command.split()
    cmd_type = cmd_list[0]
    if cmd_type == 'help' or cmd_type == 'quit' or cmd_type == 'exit':
        return cmd_type, []
    elif cmd_type == 'list':
        cmd_name = cmd_list[1]
        if cmd_name in ['show', 'create', 'use']:
            #!  cmd_list[2:] -> to prevent list index out of bound in case of no args
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []
    elif cmd_type == 'todo':
        cmd_name = cmd_list[1]
        if cmd_name in ['add', 'edit', 'remove', 'complete', 'incomplete', 'all']:
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []


def main():
    print('todo-cli application started')
    while(1):
        command = input('$ ')
        command_type = command.split()[0]
        command_name, command_arg = parse(command)
        if command == 'quit' or command == 'exit':
            break
        elif command == 'help':
            console.print(""" The following commands are available:
                  1. list show -> show all the todo lists
                  2. list create list_name -> create a list with list_name
                  3. list use list_name -> start using a particular list
                  4. todo add todo_title -> add a todo item in the selected list
                  5. todo all -> show all todos in the selected list
                  6. todo edit item_id new_title -> edit the todo item with id=item_id
                  7. todo remove item_id -> remove the todo item with id=item_id
                  8. todo complete item_id -> mark a todo item with id=item_id as complete
                  9. todo incomplete item_id -> mark a todo item with id=item_id as incomplete
                  10. help -> print all the commands provided by the app
                  11. quit or exit -> exit the application
                  """, style = "white")
        elif command_name == 'invalid':
            print("Please enter a valid command, use help command to display all!")
        elif command_name == 'use':
            print('use a particular list')  
        else:
            commands_dict[command_name](command_arg)
        

if __name__ == '__main__':
    main()