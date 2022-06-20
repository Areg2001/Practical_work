num = int(input('Please, enter the number: '))

def total_sum(number):
    res = 0
    for i in range(1, number + 1):
        res += i

    return res

print(total_sum(num))
