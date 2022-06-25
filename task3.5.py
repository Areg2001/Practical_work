word = input('Please, enter the word: ')
def str_reverse(word):
    res = ''
    for i in range(len(word)):
        res += word[len(word) - 1 - i]
        
    return res
    
print(str_reverse(word))