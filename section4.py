#try
todolist = []

while True:
    action = input("add, edit, remove, show or exit to do list? ")

    match action:
        case 'add':
            todo = input("what do you want to do? ")
            todolist.append(todo)
        case 'edit':
            edit = int(input("which item to edit? "))
            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ")
            else:
                print("learn how to count too")
        case 'remove':
            remove = int(input("which item to remove? "))
            if remove <= len(todolist):
                todolist.remove(todolist[remove-1])
            else:
                print("eeeeeeehhh wrong!!!!! stupid")
        case 'show':
            for item in todolist:
                print(item)
        case 'exit':
            break
print("see ya")

#e19
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

#e20
words = ['w' , 'o' , 'r' , 'd' , 's']
print(words[3])

#e21
language = "pytgon"
language = language.replace('g' , 'h')
print(language)

#e22
usernames = ['the blueman', 'sorted hedgehog', 'ifinite lagoon']
for item in usernames:
    item = item.replace(' ', '_')
    print(item)

#e23
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)
print(seconds)

#e24
color_codes = (('blue', 5, '5'),('red', 6, '6'),('green', 7, '7'))
for item in color_codes:
    print(item)

#e25
mood = 'fine'
strength = float(1.0)
rank = int(1)
print(mood, strength, rank)

