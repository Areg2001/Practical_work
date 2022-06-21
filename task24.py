number = None
count, res = 0, 0
while number != 0:
    number = int(input('Please, enter numbers: '))
    count += 1
    res += number

if count == 1:
    raise ZeroDivisionError('There are 0 elements')

def Arithmetic_average(numbers):
    return res/(count - 1)

print(Arithmetic_average(number))    


