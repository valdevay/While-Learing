text = list('хуgffdк') # заменить "к" на "й"

print(text)

for letter in text:
    if letter == 'к':
        letter = 'й'

print(text)


for i in range(len(text)):
    if text[i] == 'к':
        text[i] = 'й'

print(text)

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "qwertyuiopasdfghjklzxcvbnm"
text = list(text)
for index_text in range(len(text)):
    for i in range(len(alphabet)):
        if index_text == alphabet[i]:
            index_text = key[i]
print(text)