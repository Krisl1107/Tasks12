def text_ch(text, line_length):
    words = text.split()
    l = []
    c_l = []

    for word in words:
        if sum(len(w) for w in c_l) + len(c_l) + len(word) <= line_length:
            c_l.append(word)
        else:
            if c_l:
                l.append(justify_line(c_l, line_length))
            c_l = [word]

    if c_l:
        l.append(' '.join(c_l).ljust(line_length))

    return '\n'.join(l)


def justify_line(words, line_length):
    if len(words) == 1:
        return words[0].ljust(line_length)

    total_chars = sum(len(word) for word in words)
    total_spaces = line_length - total_chars
    space_between_words = total_spaces // (len(words) - 1)
    extra_spaces = total_spaces % (len(words) - 1)

    justified_line = ''

    for i in range(len(words)):
        justified_line += words[i]
        if i < len(words) - 1:
            justified_line += ' ' * (space_between_words + (1 if i < extra_spaces else 0))

    return justified_line

text_input =input()
line_length_input =int( input())
justified_text = text_ch(text_input, line_length_input)
print(justified_text)
