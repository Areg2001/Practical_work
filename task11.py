MPG = float(input('Please, enter count of MPG: '))

def changed(count_of_MPG):
    return count_of_MPG * (235.21 / 100)

print(changed(MPG))    