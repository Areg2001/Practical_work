from random import randint
lst = []
while len(lst) != 6:
    value = randint(1, 50)
    if value not in lst:
        lst.append(value)
lst.sort()   
    
print(lst)    