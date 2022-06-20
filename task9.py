initial = int(input('Please, enter amount of initial investment'))

def first_year_balance(money):
    res = money + ((money * 4) / 100)
    return res

def second_year_balance(money):
    res = first_year_balance(money) + ((first_year_balance(money)) * 4 / 100)
    return res

def third_year_balance(money):
    res = second_year_balance(money) + ((second_year_balance(money) * 4)/ 100)
    return res

print(first_year_balance(initial), second_year_balance(initial), third_year_balance(initial))             