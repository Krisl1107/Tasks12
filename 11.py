cities=input()
words = cities.split()

players = ["Петя", "Вася"]

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    if word[-1].lower() != next_word[0].lower():
        print(f"{players[i % 2]} проиграл")
print(f"{players[(len(words) - 1) % 2]} выиграл")
