def func(s):
    b=False
    for c in s:
        if c=='b':
            b=True
        if b:
            if c =='a' :
                return False
    return True
s = "abab"
print(func(s))