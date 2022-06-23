
sentence = input('Please, enter the sentecne: ')

def is_polindrom(data):
    signs = '`,.;:?'
    final_sentence = ''
    for i in data:
        if not i in signs:
            final_sentence += i
    list_of_words = final_sentence.split()

    for i in range(len(list_of_words) // 2):
        list_of_words[i] = list_of_words[i].lower()
        if list_of_words[i] != list_of_words[len(list_of_words) - 1 - i]:
            return False
    return True                

print(is_polindrom(sentence))           
