Celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def Farenheit(data):
    Fahrenheit = len(data) * [None]
    for i in range(len(data)):
        Fahrenheit[i] = (1.8 * data[i]) + 32
    return Fahrenheit    

print(f'Celsius = {Celsius}:')
print(f'Fahrenheit = {Farenheit(Celsius)}')


