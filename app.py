from commands import commands_dict
from rich.table import Table
from rich.console import Console

console = Console()

# takes the command as input and returns command_name and command_args
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
    console.print(
        "Todo CLI application started, use [bold yellow]help[/] command to get started!", style="bold blue")
    while(1):
        command = input('$ ')
        command_type = command.split()[0]

        try:
            command_name, command_arg = parse(command)

            if command == 'quit' or command == 'exit':
                break
            elif command == 'help':
                console.print(""" 
            [bold red]Commands to manipulate lists[/]:
                - [bold yellow]list show[/] -> show all the todo lists
                - [bold yellow]list create list_name[/] -> create a list with list_name
                - [bold yellow]list use list_name[/] -> start using a particular list
                
            [bold red]Commands to manipulate todo[/]:
                - [bold yellow]todo add todo_title[/] -> add a todo item in the selected list
                - [bold yellow]todo all[/] -> show all todo's in the selected list
                - [bold yellow]todo edit item_id new_title[/] -> edit the todo item with id=item_id
                - [bold yellow]todo remove item_id[/] -> remove the todo item with id=item_id
                - [bold yellow]todo complete item_id[/] -> mark a todo item with id=item_id as complete
                - [bold yellow]todo incomplete item_id[/] -> mark a todo item with id=item_id as incomplete
                
            [bold red]General-purpose commands[/]:
                - [bold yellow]help[/] -> print all the commands provided by the app
                - [bold yellow]quit[/] or [bold yellow]exit[/] -> exit the application
                    """, style="white")
            elif command_name == 'use':
                current_list = commands_dict[command_name](command_arg)
            elif command_type == 'todo':
                try:
                    command_arg.insert(0, current_list)
                    commands_dict[command_name](command_arg)
                except:
                    console.print(
                        "Kindly select or create a list first!", style="bold yellow")
            else:
                commands_dict[command_name](command_arg)
        except:
            console.print(
                "Please enter a valid command, use help command to display all!", style="bold yellow")


if __name__ == '__main__':
    main()
