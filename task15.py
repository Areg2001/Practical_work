import math
cylinder_radius = int(input('Please, enter radius of cylinder: '))
cylinder_height = int(input('Please, enter height of cylinder: '))

def circle_area(radius):
    return math.pi * (radius ** 2)

def cylinder_volume(radius, height):
    return circle_area(radius) * height 

print(cylinder_volume(cylinder_radius, cylinder_height))      
