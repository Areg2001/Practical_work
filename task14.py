import math
radius = int(input('Please, enter radius'))
r = radius

def circle_area(radius):
    return (math.pi * (r ** 2))

def ball_volume(radius):
      return (4/3 * math.pi) * (radius ** 3)  

print(circle_area(r), ball_volume(r))