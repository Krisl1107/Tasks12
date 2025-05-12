text=input()
s = []
def check(text):
 for char in text:
    if char == '(':
        s.append(char)
    elif char == ')':
        if not s:
          return False
        s.pop()
 return len(s) == 0
if check(text):
    print("Круглые скобки расставлены правильно")
else:
    print("Круглые скобки расставлены неправильно")

