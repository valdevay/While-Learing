# Задание: Записать в файл encoded_text.txt
#          зашифрованный текст с помощью
#          сгенерированного ключа

import string_utils
from alphabets import *

def generate_key(alphabet: str) -> str:
    return string_utils.shuffle(alphabet)

# key = "xyz" (a -> x, b -> y, c -> z)
# "cab" -> "zxy" 

def encode_text(text: str, alphabet: str, key: str) -> str:
    text = list(text)
    for index_text in range(len(text)):
        for i in range(len(alphabet)):
            if text[index_text] == alphabet[i]:
                text[index_text] = key[i]
                break

    return ''.join(text)

def decode_text(text: str, alphabet: str, key: str) -> str:
    text = list(text)
    for index_text in range(len(text)):
        for i in range(len(key)):
            if text[index_text] == key[i]:
                text[index_text] = alphabet[i]
                break
            
    return ''.join(text)


with open("cryptography/text.txt", "r") as f:
    original = f.read()


key = generate_key(EN_AL)
encoded = encode_text(original, EN_AL, key)
decoded = decode_text(encoded, EN_AL, key)

print("key =", key)
print("original =", original)
print("encoded =", encoded)
# # Можно вывести в отдельный файл для тренировки
print("decoded =", decoded)
