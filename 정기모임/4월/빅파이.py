word = input('단어를 입력하시오: ')
word = word.upper()
lst_word = list(word)
dict_word = {}

for i in range(len(lst_word)):
    if lst_word[i] not in dict_word:
        dict_word[lst_word[i]] = 1
    else:
        dict_word[lst_word[i]] += 1
        

most = 0
for i in dict_word:
    if dict_word[i] > most:
        most = dict_word[i]
        most_word = i
    elif dict_word[i] == most:
        most_word = '?'
    
print(most_word)