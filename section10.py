while True:
    action = input("add, edit, remove, show or exit to do list? ")

    if action.startswith('add'):
        #get item from user
        todonew = action[4:]

        #read from file and create list
        with open('todo.txt' , 'r') as file:
            todolist = file.readlines()

        #add new user to do item to the new list
        todolist.append(todonew + '\n')

        #override old file with new list of items
        with open('todo.txt' , 'w') as file:
            file.writelines(todolist)
        


    elif action.startswith('edit'):
        try:
            edit = int(action[5:])

            with open("todo.txt" , 'r') as file:
                todolist = file.readlines()

            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ") + "\n"
            else:
                print("learn how to count too")

            with open("todo.txt" , 'w') as file:
                file.writelines(todolist)
        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('remove'):
        try:
            remove = int(action[7:])

            with open('todo.txt' , 'r') as file:
                todolist = file.readlines()

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
            with open('todo.txt' , 'w') as file:
                file.writelines(todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('show'):
        with open('todo.txt' , 'r') as file:
            todolist = file.readlines()

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


#  e 60
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     percentage = value / total_value * 100
#     print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")

#  e 61
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     percentage = value / total_value * 100
#     print(f"That is {percentage}%")
# except ZeroDivisionError:
#     print("Total value cannot be zero.")
# except ValueError:
#     print("You need to enter a number. Run the program again.")

#  e 62
# colors = [11, 34, 98, 43, 45, 54, 54]
# for color in colors:
#     if color > 50:
#         print(color)

#  e 63
# passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]
# for password in passwords:
#     if len(password) < 8:
#         print(password)

#  e 64
# filenames = ["report.txt" , "downloads.txt", "success.txt", "folders.txt"]
# for filename in filenames:
#     if filename.endswith('.txt'):
#         print(filename[:-4])
#     else:
#         print(filename)
    
#  e 65
# filenames = ["report.txt" , "downloads.txt", "success.txt", "folders.txt"]
# for filename in filenames:
#     if filename.endswith('.txt'):
#         print(filename[:-4].capitalize())
#     else:
#         print(filename.capitalize())