text=input()
m_c = 0
c = 0
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        c += 1
    else:
        if c > m_c:
            m_c = c
            c = 0

if c > m_c:
 m_c = c

print( m_c)
