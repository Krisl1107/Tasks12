text=input()
w=text.split()
srt= sorted(w, key=len)

print(*srt)
