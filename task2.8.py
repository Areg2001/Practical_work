larger = [2, 4, 1, 8, 5]
smaller = [4, 1]
def isSublist(data1, data2):
    lists = [[]]
    for i in range(len(data1) + 1):
        for j in range(i):
            lists.append(data1[j:i])

    for i in range(len(lists) - 1):
        if data2 == lists[i]:
            return True
            
    return False                


    
print(isSublist(larger, smaller))        
                    