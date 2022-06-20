length = int(input('Please, enter length of plot(funts): '))
width = int(input('Please, enter width of plot(funts): '))

def plot_area_akr(length, width):
    return ((length * width) / 43560)

print(plot_area_akr(length, width))