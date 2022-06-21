import math
first_side = float(input('Please, enter the value of first side: '))
second_side = float(input('Please, enter the value of second side: '))
third_side = float(input('Please, enter the value of theird side: '))

s = ((first_side + second_side + third_side) / 2)

def triangle_area(a, b, c):
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print (triangle_area(first_side, second_side, third_side))    