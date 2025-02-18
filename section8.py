while True:
    action = input("add, edit, remove, show or exit to do list? ")

    match action:
        case 'add':
            #get item from user
            todo = input("what do you want to do? ") + "\n"

            #read from file and create list
            with open('todo.txt' , 'r') as file:
                todolist = file.readlines()

            #add new user to do item to the new list
            todolist.append(todo)

            #override old file with new list of items
            with open('todo.txt' , 'w') as file:
                file.writelines(todolist)


        case 'edit':
            edit = int(input("which item to edit? "))

            with open("todo.txt" , 'r') as file:
                todolist = file.readlines()

            
            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ") + "\n"
            else:
                print("learn how to count too")

            with open("todo.txt" , 'w') as file:
                file.writelines(todolist)


        case 'remove':
            remove = int(input("which item to remove? "))

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
            


        case 'show':
            with open('todo.txt' , 'r') as file:
                todolist = file.readlines()

            #list comprehension
            # newlist = [item.strip("\n") for item in todolist]

            #iterate list to show items
            for index,item in enumerate(todolist):
                item = item.strip('\n')
                list_item = f"{index + 1}: {item}"
                print(list_item)


        case 'exit':
            break
print("see ya")

# e 48
# with open("bear.txt" , 'r') as file:
#     content = file.read()
# print(content)

# e 49
# with open("essay.txt", 'r') as file:
#     content = file.read()
# nr_chars = len(content)
# print(nr_chars)

# e 50
# with open('file.txt', 'w') as file:
#     file.write('snail')

# e 51
# languages = ['English', 'German', 'Spanish']
# for language in languages:
#     with open(f"{language}.txt" , 'w') as file:
#         file.write(language)

# with open(f"/Users/deni/Development/udemypy/folders/{language}.txt" , 'w') as file:

# e 52
# with open('story.txt' , 'r') as file:
#     story = file.read()

# with open('story_copy.txt' , 'w') as file:
#     file.write(story)

# bonus example journal s 83
# from datetime import date
# todaysdate = date.today()
# print(todaysdate)
# day_rating = input("how would you rate your mood today between 1 and 10?: ") + '\n\n'
# journal = input("how was your day?\n")

# with open(f'/Users/deni/Development/udemypy/folders/{todaysdate}.txt' , 'w') as file:
#     file.write(day_rating)
#     file.write(journal)
