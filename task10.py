import math
a = int(input('Please, enter the first number: '))
b = int(input('Please, enter the second number: '))

def sum_(a, b):
    return a + b

def substraction(a, b):
    return a - b

def division(a, b):
    return a / b

def whole_part(a, b):
    return a // b

def residual(a, b):
    return a % b

def log_(a):
   return math.log(a)

print(sum_(a, b), substraction(a, b), division(a, b), whole_part(a, b), residual(a, b), log_(a))      
