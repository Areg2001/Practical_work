import math
height = int(input('Please, enter height in metrs: '))

def speed_of_object(height):
    return math.sqrt(2 * 9.8 * height)

print(speed_of_object(height))    