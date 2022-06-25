number = int(input())
def reverse_number(data):
    res, num, count = 0, data, 0
    while num > 9:
        num = num // 10
        count += 1
    while data != 0:
        res += (data % 10) * (10 ** count)
        data = data // 10
        count -= 1
        
    return res
    
print(reverse_number(number))    
        