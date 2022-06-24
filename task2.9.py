list1 = [1, 3, 2, 4, 5]
list2 = [3, 6, 7, 1, 2]
def zip(data1, data2):
    lists = []
    for i in range(len(data1)):
        lists.append([data1[i], data2[i]])
    return lists
        
print(zip(list1, list2))    