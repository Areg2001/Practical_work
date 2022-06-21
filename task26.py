def is_divided_into_3(a):
    return a % 3 == 0

def is_divided_into_5(a):
    return a % 5 == 0

def is_divided_both_of_3_and_5(a):
    return a % 15 == 0
    
variable = 1

while variable <= 100:
    if is_divided_both_of_3_and_5(variable):
        print('Fizz-Buzz')
    elif is_divided_into_3(variable):
        print('Fizz')
    elif is_divided_into_5(variable):
        print('Buzz')   
    else:
        print(variable)     
    variable += 1