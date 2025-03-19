# from functions import get_read_file, write_file
import functions

while True:
    action = input("add, edit, remove, show or exit to do list? ")

    if action.startswith('add'):
        #get item from user
        todonew = action[4:]

        todolist = functions.get_read_file()

        #add new user to do item to the new list
        todolist.append(todonew + '\n')

        #override old file with new list of items
        functions.write_file(todolist)
        


    elif action.startswith('edit'):
        try:
            edit = int(action[5:])

            todolist = functions.get_read_file()

            if edit <= len(todolist):
                todolist[edit-1] = input("new to do: ") + "\n"
            else:
                print("learn how to count too")

            functions.write_file(todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('remove'):
        try:
            remove = int(action[7:])

            todolist = functions.get_read_file()

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
            functions.write_file(todolist)

        except ValueError:
            print("invalid try again")
            continue


    elif action.startswith('show'):
        todolist = functions.get_read_file()

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


#########################
#section 127

feet_inches = input("enter height in feet and inches ")

def split(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    #return list or touple of results, but by default returning two variables will automatically return a touple
    return feet, inches
   
def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = split(feet_inches)
height = convert(f, i)
if height > 1:
    print(height , " is fine")
else:
    print(height , "is too small for fun")

# e 76
birth_year = input("what year were you born in? ")
def get_age(year_of_birth, current_year = 2025):
    age = current_year - int(year_of_birth)
    return age

print(get_age(birth_year))

# e 77
string = "john,lisa, teresa,  maria"
def get_nr_items(user_input):
    list = user_input.split(",")
    return len(list)

print(get_nr_items(string))

# e 78
def get_area(a):
    return a * a

# e 79
def weather(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"    
print(weather(8))

# e 80
def passwordlen(password):
    if len(password) < 8:
        return False
    else:
        return True
print(passwordlen("short"))    
print(passwordlen("mystrongpassword"))
