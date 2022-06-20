less = int(input('Please, enter count of bottles that are less than 1 liter: '))
big = int(input('Please, enter count of bottles that are bigger than 1 liter: '))

def total_amount(less, big):
    return (less * 0.10) + (big * 0.25)

print(f'${(total_amount(less, big)):.2f}')    
