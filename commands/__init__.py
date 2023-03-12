import commands.lists
import commands.todos

# map command name to the respective command function
commands_dict = {
    'show': lists.show_lists,
    'use': lists.use_list,
    'create': lists.create_list,
    'drop': lists.drop_list,
    'add': todos.add_item,
    'all': todos.show_items,
    'edit': todos.edit_item,
    'remove': todos.remove_item,
    'complete': todos.mark_item_complete,
    'incomplete': todos.mark_item_incomplete
}