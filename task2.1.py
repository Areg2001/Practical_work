words = None
res = []
while words != '':
    words = input('Please, enter words: ')
    if words not in res:
        res.append(words)
del res[-1]        

def final_list_of_words(words):
    return words

print(final_list_of_words(res))            



