def get_read_file(filepath):
    with open(filepath , 'r') as file:
        todolist = file.readlines()
    return todolist

# pass the list to the function
def write_file(filepath , data):
    with open(filepath , 'w') as file:
        file.writelines(data)


while True:
    action = input("add, edit, remove, show or exit to do list? ")

    if action.startswith('add'):
        #get item from user
        todonew = action[4:]

        todolist = get_read_file("todo.txt")

        #add new user to do item to the new list
        todolist.append(todonew + '\n')

        #override old file with new list of items
        write_file("todo.txt" , todolist)
        


    elif action.startswith('edit'):
        try:
            edit = int(action[5:])

            todolist = get_read_file("todo.txt")

            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ") + "\n"
            else:
                print("learn how to count too")

            write_file("todo.txt" , todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('remove'):
        try:
            remove = int(action[7:])

            todolist = get_read_file("todo.txt")

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
            write_file("todo.txt" , todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('show'):
        todolist = get_read_file("todo.txt")

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


#################

# section 118 
feet_inches = input("enter height in feet and inches ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters

height = convert(feet_inches)
if height > 1:
    print(height , " is fine")
else:
    print(height , "is too small for fun")

# e 70
def liters_to_m3(liters):
    m3 = liters / 1000
    return m3

# e 71
password = input("try password: ")
def strength(password):
    if len(password) > 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Strong Password"
    else:
        return "Weak Password"

result = strength(password)
print(result)

# e 72
numbers = [1 , 2 , 3 , 4 , 5 , 6]

def get_average(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    average = sum / len(numbers)
    return average

print(get_average(numbers))

# e 73
original = "felicia"

def function(name):
    return f"Hi {name}"

print(function(original))

# e 74
string1 = "hey "
string2 = "there"

def get_string(a , b):
    string = a + b
    return string

print(get_string(string1 , string2))

# e 75
original = "felicia"

def function(name):
    name = name.capitalize()
    return f"Hi {name}"

print(function(original))