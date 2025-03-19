# e 81
def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif temperature > 0 and temperature <100:
        return "Liquid"
    elif temperature >= 100:
        return "Gas"
    
print(water_state(0))

# e 82
FREEZING_POINT = 0
BOILING_POINT = 100
def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature > FREEZING_POINT and temperature <BOILING_POINT:
        return "Liquid"
    elif temperature >= BOILING_POINT:
        return "Gas"
print(water_state(99))

# e 83
def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    elif temperature < 15:
        return "Cold"

print(foo(14))