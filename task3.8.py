date = int(input('Please, enter date: '))
month  = int(input('Please, enter number of month: '))
def is_leap_year(data):
    return data % 4 == 0 and data % 100 != 0
    
days30 = [4, 6, 9, 11]
days31 = [1, 3, 5, 7, 8, 10, 12]

def days_of_month(date, month):
    if month in days30:
        return 30
    elif month in days31:
        return 31
    elif is_leap_year(date):
        return 29
        
    return 28
    
print(days_of_month(date, month))    