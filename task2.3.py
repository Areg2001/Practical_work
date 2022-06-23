number = int(input('Please, enter the number: '))
def is_perfect(a):
    return sum([i for i in range(1, a) if a % i == 0]) == a

print(is_perfect(number))    
