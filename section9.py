# while True:
#     action = input("add, edit, remove, show or exit to do list? ")

#     if 'add' in action:
#         #get item from user
#         todonew = action[4:]

#         #read from file and create list
#         with open('todo.txt' , 'r') as file:
#             todolist = file.readlines()

#         #add new user to do item to the new list
#         todolist.append(todonew)

#         #override old file with new list of items
#         with open('todo.txt' , 'w') as file:
#             file.writelines(todolist)


#     elif 'edit' in action:
#         edit = int(action[5:])

#         with open("todo.txt" , 'r') as file:
#             todolist = file.readlines()

#         if edit <= len(todolist):
#             todolist[edit-1] = input("new to do: ") + "\n"
#         else:
#             print("learn how to count too")

#         with open("todo.txt" , 'w') as file:
#             file.writelines(todolist)


#     elif 'remove' in action:
#         remove = int(action[7:])

#         with open('todo.txt' , 'r') as file:
#             todolist = file.readlines()

#         #store the item that you want removed so you can display it 
#         remove_item = todolist[remove-1].strip('\n') 
#         # remove_item = remove_item.strip('\n')

#         # removes from the list but not from the file
#         if remove <= len(todolist):
#             todolist.remove(todolist[remove-1])
#         else:
#             print("eeeeeeehhh wrong!!!!! stupid")

#         removed = f"item {remove}: {remove_item} - is now off the to do list"
#         print(removed)

#         #override the file with the new list
#         with open('todo.txt' , 'w') as file:
#             file.writelines(todolist)
            

#     elif 'show' in action:
#         with open('todo.txt' , 'r') as file:
#             todolist = file.readlines()

#         #list comprehension
#         # newlist = [item.strip("\n") for item in todolist]

#         #iterate list to show items
#         for index,item in enumerate(todolist):
#             item = item.strip('\n')
#             list_item = f"{index + 1}: {item}"
#             print(list_item)

#     elif 'exit' in action:
#         break
#     else:
#         print("option not available try again")

# print("see ya")


#  e 53
# password = input("Enter a new password: ")
# if len(password) >= 7:
#     print("Great password there!")
# else:
#     print("Your password is weak.")


#  e 54
# password = input("Enter a new password: ")
# if len(password) > 7:
#     print("Great password there!")
# elif len(password) == 7:
#     print("Password is OK, but not too strong")
# else:
#     print("Your password is weak")


#  e 55
# day_temperatures = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}

#  e 56
day_temperatures = {'morning':(1.1 , 2.2 , 3.3) , 'noon':(4.4 , 5.5 , 6.6) , 'evening':(7.7 , 8.8 , 9.9)}

#  e 57
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

#  e 58
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0:3])

#  e 59
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[4:])