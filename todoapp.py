def read_list():
    with open("todo.txt" , 'r') as file:
        todolist = file.readlines()
    return todolist

# pass the list to the function
def write_list(data):
    with open("todo.txt" , 'w') as file:
        file.writelines(data)


while True:
    action = input("add, edit, remove, show or exit to do list? ")

    if action.startswith('add'):
        #get item from user
        todonew = action[4:]

        todolist = read_list()

        #add new user to do item to the new list
        todolist.append(todonew + '\n')

        #override old file with new list of items
        write_list(todolist)
        


    elif action.startswith('edit'):
        try:
            edit = int(action[5:])

            todolist = read_list()

            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ") + "\n"
            else:
                print("learn how to count too")

            write_list(todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('remove'):
        try:
            remove = int(action[7:])

            todolist = read_list()

            #store the item that you want removed so you can display it 
            remove_item = todolist[remove-1].strip('\n') 
            # remove_item = remove_item.strip('\n')

            # removes from the list but not from the file
            if remove <= len(todolist):
                todolist.remove(todolist[remove-1])
            else:
                print("eeeeeeehhh wrong!!!!! stupid")

            removed = f"item {remove}: {remove_item} - is now off the to do list"
            print(removed)

            #override the file with the new list
            write_list(todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('show'):
        todolist = read_list()

        #list comprehension
        # newlist = [item.strip("\n") for item in todolist]

        #iterate list to show items
        for index,item in enumerate(todolist):
            item = item.strip('\n')
            list_item = f"{index + 1}: {item}"
            print(list_item)


    elif action.startswith('exit'):
        break
    
    
    else:
        print("option not available try typing the action first")

print("see ya")