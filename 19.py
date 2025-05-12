def justify_text(text, line_length):
    words = text.split()
    lines = []
    current_line = []

    for word in words:

        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= line_length:
            current_line.append(word)
        else:

            if current_line:
                lines.append(justify_line(current_line, line_length))

            current_line = [word]


    if current_line:
        lines.append(' '.join(current_line).ljust(line_length))

    return '\n'.join(lines)


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



text_input = input()
line_length_input = 30

justified_text = justify_text(text_input, line_length_input)
print(justified_text)
