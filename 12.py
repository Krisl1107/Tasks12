mport keyword

def identifier_ch(id):
    if id in keyword.kwlist:
        return False

    if not id[0].isalpha() and id[0] != '_':
        return False
    for char in id:
        if not (char.isalnum() or char == '_'):
            return False
    return True

str = input()
if identifier_ch(str):
    print(f'"{str}" может быть именем в языке Python.')
else:
    print(f'"{str}" не может быть именем в языке Python.')
