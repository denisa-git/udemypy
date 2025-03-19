def get_read_file(filepath = 'todo.txt'):
    """gets the items from file and returns a list of them"""
    with open(filepath , 'r') as file:
        todolist = file.readlines()
    return todolist

# pass the list to the function
def write_file(data , filepath = 'todo.txt'):
    """writes list to file"""
    with open(filepath , 'w') as file:
        file.writelines(data)
