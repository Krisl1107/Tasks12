text=input()
k=[]
for ch in text:
    if ch not in k:
        k.append(ch)
print(len(k))
