# while True:
#     action = input("add, edit, remove, show or exit to do list? ")

#     match action:
#         case 'add':
#             #get item from user
#             todo = input("what do you want to do? ") + "\n"
#             #open file to read from 
#             file = open('todo.txt' , 'r')
#             #create list with existing items from opened file
#             todolist = file.readlines()
#             #close file every time 
#             file.close()
#             #add new user item to the new list
#             todolist.append(todo)

#             #override old file with new list of items
#             file = open('todo.txt' , 'w')
#             #write the new list of items in the overridden file
#             file.writelines(todolist)
#             #close file every time
#             file.close()

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
#             #open file in read mode
#             file = open('todo.txt' , 'r')
#             #create list with existing items in file
#             todolist = file.readlines()
#             file.close()

#             #iterate list to show items
#             for item in todolist:
#                 counter = todolist.index(item) + 1
#                 print(counter, ': ', item)
#         case 'exit':
#             break
# print("see ya")

# experiment writing things to multiple files
# contents = ["this will be in file1!" , "this will be in file2!" , "this will be in file3!"]
# filenames = ["file1.txt" , "file2.txt" , "file3.txt"]
# for content, filename in zip(contents, filenames):
#     file = open(f"folders/{filename}" , 'w')
#     file.write(content)

# e 36
# open bear.txt and write out the content
# file = open("/Users/deni/Development/udemypy/folders/bear.txt" , 'r')
# content = file.read()
# print(content)

# e 37
# file = open("/Users/deni/Development/udemypy/folders/essay.txt" , 'r')
# content = file.readlines()
# file.close()
# print(content.title())

# e 38
# file = open("/Users/deni/Development/udemypy/folders/essay.txt" , 'r')
# content = file.read()
# file.close()
# print(len(content))

# e 39
# file = open("/Users/deni/Development/udemypy/folders/essay.txt" , 'r')
# # file = open("essay.txt" , 'r')
# content = file.read()
# file.close()
# print('The file contains' , len(content) , 'characters.')

# e 40
# file = open("/Users/deni/Development/udemypy/folders/file.txt" , 'w')
# # file = open("file.txt" , 'w')
# file.writelines("snail")
# file.close()

# e 41
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
# for country , filename in zip(countries , filenames):
#     file = open(f"/Users/deni/Development/udemypy/folders/{filename}" , 'w')
#     file.write(country)
#     file.close()

# e 42
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# for country in countries:
#     file = open(f"/Users/deni/Development/udemypy/folders/{country}.txt" , 'w')
#     file.write(country)
#     file.close()

# section 64
# new = input("add a new member: ")

# file = open("/Users/deni/Development/udemypy/folders/members.txt" , 'r')
# members = file.readlines()
# file.close()

# members.append("\n\n" + new)
# file = open("/Users/deni/Development/udemypy/folders/members.txt" , 'w')
# members = file.writelines(members)
# file.close()

# section 65
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for filename in filenames:
#     file = open(f"/Users/deni/Development/udemypy/folders/{filename}" , 'w')
#     file.write("hello")
#     file.close()

files = ['/Users/deni/Development/udemypy/folders/a.txt' ,
              '/Users/deni/Development/udemypy/folders/b.txt' ,
              '/Users/deni/Development/udemypy/folders/c.txt']

for file in files:
    file = open(file , 'r')
    print(file.read())
    file.close()
