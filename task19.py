count_of_days = int(input('Please, enter count of days: '))
count_of_hours = int(input('Please, enter count of hours: '))
count_of_minutes = int(input('Please, enter count of minutes: '))
count_of_seconds = int(input('Please, enter count of seconds: '))

def days_total_seconds(a):
    return ((a * 24) * 3600)

def hours_total_seconds(b):
    return b * 3600

def minutes_total_seconds(c):
    return c * 60
    
def total_seconds(a, b, c):
    return days_total_seconds(a) + hours_total_seconds(b) + minutes_total_seconds(c) + count_of_seconds

print(total_seconds(count_of_days, count_of_minutes, count_of_minutes))   
