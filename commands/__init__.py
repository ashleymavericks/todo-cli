import commands.lists
import commands.todos

# map command name to the respective command function
commands_dict = {
    'show': lists.show_lists,
    'use': lists.use_list,
    'create': lists.create_list,
    'add': todos.add_item,
    'all': todos.show_items
}