s = "(()())(())(()(()))"
res=""
c = 0
for i in range(len(s)):
    if (s[i] == '(') :
        if (c > 0) :
            res += s[i]; 
        c+=1 
    else :
        c-=1
        if (c > 0) :
            res += s[i]
print(res)