lst = [1, 3, 4, 8, 5]
def is_even(data):
    return len(data) % 2 == 0

def is_even_median(data):
    return (data[(len(data) // 2) - 1] + data[len(data) // 2]) / 2
    
def get_median(data):
    return is_even_median(data) if is_even(data) else data[len(data) // 2]
    
print(f'It is median of this list: {get_median(lst)}')    