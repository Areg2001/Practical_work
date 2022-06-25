number = int(input('Please, enter the number: '))
def is_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True        
        
def smallest_prime(n):
    if is_simple(n):
        n += 1
    while not is_simple(n):
        n += 1
        
    return n
    
print(f'Large from {number} and the smallest simple number is: {smallest_prime(number)}') 