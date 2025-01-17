# try to show the numbers index of the list items
# todolist = []

# while True:
#     action = input("add, edit, remove, show or exit to do list? ")

#     match action:
#         case 'add':
#             todo = input("what do you want to do? ")
#             todolist.append(todo)
#         case 'edit':
#             edit = int(input("which item to edit? "))
#             if edit <= len(todolist):
#                 todolist[edit-1] = input("new to do: ")
#             else:
#                 print("learn how to count too")
#         case 'remove':
#             remove = int(input("which item to remove? "))
#             if remove <= len(todolist):
#                 todolist.remove(todolist[remove-1])
#             else:
#                 print("eeeeeeehhh wrong!!!!! stupid")
#         case 'show':
#             for item in todolist:
#                 counter = todolist.index(item) + 1
#                 print(counter, ': ', item)
#         case 'exit':
#             break
# print("see ya")

# to remove
# remove = int(input("number of the list to remove? "))
# todolist.pop(remove)

# e26
# temperatures = [10.11, 10, 'numbers']

# e27
# rainfall = [10.5, 11, 'cold', [20.5, 21, 'warm']]

# e28
# furniture = ['table', 'chair', 'door']
# for index, item in enumerate(furniture):
#     print(index, ':', item)

# e29
# products = ['table','chair', 'door']
# for index, item in enumerate(products):
#     print('Products: ', item)

# e30
# filenames = ['document', 'report', 'presentation']
# for index, item in enumerate(filenames):
#     f = f"{index}-{item}.txt"
#     print(f)

# e31
# filenames = ['document', 'report', 'presentation']
# for index, item in enumerate(filenames):
#     item = item.capitalize()
#     look = f"{index}-{item}.txt"
#     print(look)

# e32
# seconds = [1.23, 1.45, 1.02, 1.11]
# seconds.pop(1)
# print(seconds)

# try
# how = enumerate("hello")
# print(list(how))

# e33
# mystring = "mystring"
# mylist = ["m", "y", "l"]
# print(len(mystring), " ; ", len(mylist))

# e34
# mylist = ['a', 'b', 'c', 'd']
# for item in mylist:
#     print(len(mylist))

# try 53
names = ["kevin", "john", "katy", "other", "classic", "names"]
names.sort()
for index, item in enumerate(names):
    print(f"{index + 1}. {item.capitalize()}")

# e35
measurements = [177.8, 175.8, 166.9, 182.5]
measurements.sort()
for item in measurements:
    print(item)