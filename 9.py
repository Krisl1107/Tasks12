text=input()
w=text.split()
c_w={}

for word in w:
    c_w[word]=c_w.get(word,0)+1
n=[word for word, count in c_w.items() if count==2]
print(n)
