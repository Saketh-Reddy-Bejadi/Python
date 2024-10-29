import math
def valid(s):
    l = len(s)
    c = int(math.ceil(l**(0.5)))
    a = ""
    for i in range(c):
        k = i
        for j in range(k,l,c):
            a+=s[j]
        a+=" "
    return a

s="haveaniceday"
print(valid(s))