def missingCharacters(s):
    ref='0123456789abcdefghijklmnopqrstuvwxyz'
    
    
    res=[char for char in ref if char not in s]
    return str(res)
s = input()
result = missingCharacters(s)
print(str(result))
