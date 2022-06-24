inp = input()
lst = []
while len(inp) != 0:
    lst.append(int(inp))
    inp = input()

def arithmetic_average(data):
    return sum(data) / len(data)

def from_small_to_large(data):
    data.sort()
    return data

print(arithmetic_average(lst))
print(from_small_to_large(lst))    
