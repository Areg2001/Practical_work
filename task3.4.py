lst = [2, 6, 8, 5, 1, 18, 7, 9, 86]
def is_even(data):
    return data % 2 == 0

def even_indexes_of_arr(data):
    return [i for i in range(len(data)) if is_even(data[i])]
    
print(even_indexes_of_arr(lst))    