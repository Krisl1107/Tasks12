def number_to_words(n):
    if n == 0:
        return "ноль"

    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста",
                "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    thousands = ["тысяча"] + ["тысячи"] * 4 + ["тысяч"] * 6
    millions = ["миллион"] + ["миллиона"] * 4 + ["миллионов"] * 6

    words = []

    if n >= 1000000:
        million_part = n // 1000000
        words.append(number_to_words(million_part))
        words.append(millions[min(million_part % 10, 9)])

        n %= 1000000

    if n >= 1000:
        thousand_part = n // 1000
        words.append(number_to_words(thousand_part))
        words.append(thousands[min(thousand_part % 10, 9)])

        n %= 1000

    if n >= 100:
        words.append(hundreds[n // 100])
        n %= 100

    if n >= 20:
        words.append(tens[n // 10])
        n %= 10

    if n >= 10:
        words.append(teens[n - 10])
        n = 0

    if n > 0:
        words.append(units[n])

    return ' '.join(filter(None, words)).strip()


number = int(input("Введите натуральное число (не больше 900000000): "))
print(number_to_words(number))
