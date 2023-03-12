from commands import commands_dict


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
        elif command_name == 'invalid':
            print('Please enter a valid command')
        elif command_name == 'use':
            print('use a particular list')  
        else:
            commands_dict[command_name](command_arg)
        

if __name__ == '__main__':
    main()