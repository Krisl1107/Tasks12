text= input()
def unique_letters(word):
    return len(word) == len(set(word))

words = text.split()

f_word = words[0]
unique_words = []

for word in words:
    if word != f_word and unique_letters(word):
        unique_words.append(word)

print(unique_words)
