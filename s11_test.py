# def greet():
#     message = 'hello'
#     new_mes = message.capitalize()
#     print("sup")
#     return new_mes


# greet()
# print(greet())

def get_average():
    with open("/Users/deni/Development/udemypy/folders/report.txt" , 'r') as file:
        temperatures = file.readlines()
    temperatures = temperatures[1:]
    temperatures = [float(i) for i in temperatures]

    average = sum(temperatures) / len(temperatures)
    
    return average

average = get_average()
print(average)