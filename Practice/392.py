def valid(s,t):
    ind=float('-inf')
    res=""
    for i in range(len(s)):
        if s[i] in t and t[::-1].index(s[i])>ind:
            res+='1'   
            ind=t.index(s[i])
        else :
            res+='0'
    return ('0' not in res)
s = "abc"
t = "ahbgdc"
print(valid(s,t))::