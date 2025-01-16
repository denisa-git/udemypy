#try
# todolist = []
# while True:
#     choice = input("choose now, later or never: ")
#     match choice:
#         case 'now':
#             chore = input("what? ")
#             todolist.append(chore)
#         case 'later':
#             print(todolist)
#         case 'never':
#             break    

#e14
# country = 'Italy'
# match country:
#     case 'USA':
#         print("Hello")
#     case 'Italy':
#         print("Ciao")
#     case 'Germany':
#         print("Hallo")
#     case _:
#         print("n/a")

#e15
# members = ["john","sarah","dora"]
# for i in members:
#     i = i.capitalize()
#     print(i)

#e16
# country = "USA"
# match country:
#     case 'USA' | "United States":
#         print("Hello")
#     case 'Italy':
#         print("Ciao")
#     case 'Germany':
#         print("Hallo")

#e17
# employees = ["john smith", "sarah bremen", "dora dawson"]
# for item in employees:
#     item = item.title()
#     print(item)

#e18
scores = [11, 34, 98, 43, 45,54, 54]
for item in scores:
    print(item)