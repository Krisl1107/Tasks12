text=input()
m_spaces = 0
spaces = 0
for char in text:
    if char == ' ':
        spaces += 1
    else:
        if spaces > m_spaces:
            m_spaces = spaces
            spaces = 0

if spaces > m_spaces:
 m_spaces = spaces

print( m_spaces)
