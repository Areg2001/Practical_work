tupl = (1, 4, 2, 9)
def numbers_connection(data):
    res = ''
    for i in range(len(data)):
        res += str(data[i])
        
    return int(res)
    
print(numbers_connection(tupl))    