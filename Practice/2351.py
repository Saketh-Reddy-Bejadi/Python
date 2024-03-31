def fun(s):
    seen = []
    for i in s:
        if i in seen:
            return i
        seen.append(i)
    return None
s="keelbhk"
print(fun(s))