import time
name_of_month = input(('Please, enter name of month: '))

def number_of_month(a):
    if a == 'Petrvar':
        message = f'Can be {28} or {29} days'
        return message

    return f'Cane be {30} or {31} days'

print(number_of_month(name_of_month))    
    