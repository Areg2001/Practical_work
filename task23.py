name_of_month = input('Please, enter name of month: ')
day_of_month = input('Please, enter day of month: ')
winter = ['January', 'February', 'December']
summer = ['June', 'July', 'August']
autumn = ['September', 'November', 'October']
spring = ['May', 'April', 'Mart']

if name_of_month in winter:
    print('Winter')
elif name_of_month in summer:
    print('Summer')
elif name_of_month in autumn:
    print('Autumn')
elif name_of_month in spring:
    print('Spring')            


