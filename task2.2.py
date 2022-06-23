number = int(input('Please, enter the number: '))
def count_of_divisiors(a):
    return len([i for i in range(1, a+1) if a % i == 0])

print(count_of_divisiors(number))    
