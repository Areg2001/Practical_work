def same_parity(n, *args):
    lst = []
    for i in range(len(args)):
        if args[i] % n == 0:
            lst.append(args[i])
                
    return lst   
       
print(same_parity(2, 6, 8, 0, 4, 2, 6, 7, 9, 5, 3, 2, 8))    
        