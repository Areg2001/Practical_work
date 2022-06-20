money = int(input('Please, enter restaurant order amount: '))

def tip(total):
    return (total * 18) / 100

def taxes(total):
    return ((total * 20) / 100) 

def total_amount(total):
    return total + tip(total) + taxes(total)  

print(f'Tip = {tip(money):.2f}, Taxes = {taxes(money):.2f}, Total amount = {total_amount(money):.2f}' )  