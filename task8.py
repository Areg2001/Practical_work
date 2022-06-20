count_of_souviners = int(input('Please, enter count of purchase souviner: '))
count_of_details = int(input('Please, enter count of purchase details: '))

def total_weight(data1, data2):
    return (data1 * 75) + (data2 * 112)

print(f'{total_weight(count_of_souviners, count_of_details)}gram')    