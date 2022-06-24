numbers = input('Please, enter the first number: ')
lst = []
while numbers != '':
    lst.append(int(numbers))
    numbers = input('Please, enter the numbers: ')    
message = 'This list is sorted from the beginning: '
print(message)

def is_sorted(data):
    return sorted(data ,reverse = True) == data or sorted(data) == data

print(is_sorted(lst))    
    


