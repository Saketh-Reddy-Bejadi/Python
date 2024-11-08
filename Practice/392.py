def valid(s,t):
    i=j=0
    sLen=len(s)
    tLen=len(t)
    while i<sLen and j<tLen:
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==sLen
s = "abc"
t = "ahbgdc"
print(valid(s,t)) 