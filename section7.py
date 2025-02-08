while True:
    action = input("add, edit, remove, show or exit to do list? ")

    match action:
        case 'add':
            #get item from user
            todo = input("what do you want to do? ") + "\n"
            #open file to read from
            file = open('todo.txt' , 'r')
            #create list with existing items from opened file
            todolist = file.readlines()
            #close file every time
            file.close()
            #add new user item to the new list
            todolist.append(todo)

            #override old file with new list of items
            file = open('todo.txt' , 'w')
            #write the new list of items in the overridden file
            file.writelines(todolist)
            #close file every time
            file.close()


        case 'edit':
            edit = int(input("which item to edit? "))
            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ")
            else:
                print("learn how to count too")


        case 'remove':
            remove = int(input("which item to remove? "))

            file = open("todo.txt" , 'r')
            todolist = file.readlines()
            file.close()

            #this removes from the list but not from the file
            if remove <= len(todolist):
                todolist.remove(todolist[remove-1])
            else:
                print("eeeeeeehhh wrong!!!!! stupid")

            #override the file with the new list
            file = open("todo.txt" , 'w')
            file.writelines(todolist)
            file.close()


        case 'show':
            #open file in read mode to get the to do list items
            file = open('todo.txt' , 'r')
            #create list with existing items in file
            todolist = file.readlines()
            file.close()

            #list comprehension
            # newlist = [item.strip("\n") for item in todolist]

            #iterate list to show items
            for item in todolist:
                # item's index will start at 0, in order to display list, must add 1
                counter = todolist.index(item) + 1
                # remove the new line from each item
                space = item.strip("\n")
                print(counter, ': ', space)


        case 'exit':
            break
print("see ya")

# section 74
# filenames = ["1.doc" , "1.report" , "1.presentation"]
# filenames = [item.replace('.' , '-') + '.txt' for item in filenames]
# print(filenames)

# e 43
# names = ["john smith", "jay santi", "eva kuki"]
# names = [item.title() for item in names]
# print(names)

# # e 44
# usernames = ["john 1990", "alberta1970", "magnola2000"]
# usernames = [len(user) for user in usernames]
# print(usernames)

# # e 45
# user_entries = ["10", "19.1", "20"]
# user_entries = [float(entry) for entry in user_entries]
# print(user_entries)

# # e 46
# numbers = [10, 20, 30]
# numbers = [number*2 for number in numbers]
# print(numbers)

# # e 47
# user_entries = ['10', '19.1', '20']
# sum = 0
# for item in user_entries:
#     sum = float(item) + sum
# print(sum)