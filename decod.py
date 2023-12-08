a = '''Br Wocry, Mg Fyirls.
Emecg gnhy mils.
Br bnymvrdd, dtoervrdd, vijr xocry.
Ynh ehc xocry ilcn o phe, ic qrpnmrd ctr phe.
Ynh ehc xocry ilcn o qnccvr, ic qrpnmrd ctr qnccvr.
Ynh ehc ic ilcn o croenc, ic qrpnmrd ctr croenc.
Nnx xocry pol bvnx ny ic pol pyodt.
Br xocry, mg byirls.'''
text = list(a.lower())

en_al = 'abcdefghijklmnopqrstuvwxyz'
freq_symb = 'etoairnpsubcmwylhfdkgjqvxz' # статистика частиты символов в англ языке
freq_text = 'crnoyiedhlmpxbvqtgsfjwakuz' # статистика частоты символов в тексте
test_symb = 'teoairnpsubcmwylhfdkgjqvxz'

def get_hist(text, alphabet):

    count_symbols = {}

    # заполняем словарь нулевыми значениями    
    for i in alphabet:
        count_symbols[i] = 0

    # считаем частоту символов в тексте
    for i in text:   
        if i.isalpha():
            count_symbols[i] += 1

    # сортируем символы по частоте
    most_popular = sorted(count_symbols.items(), key=lambda x: x[1], reverse=True)

    # символы остортированные по частоте в виде строки
    letters_sorted = "".join(dict(most_popular).keys())
    
    return letters_sorted

print(get_hist('Nnx xocry pol bvnx ny ic pol pyodt.'.lower(), 'abcdefghijklmnopqrstuvwxyz'))

# соотнести символы по количеству совпадений

def decoder():

# for i in range(len(text)):
#     index = freq_text.find(text[i])
#     if index > 0:
#         text[i] = test_symb[index]
# print("".join(text))

# print(letters_sorted)

#def decoding(text,symbols):
#count_symbols
   



#decoding()