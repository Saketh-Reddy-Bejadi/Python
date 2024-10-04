def valid(s):
    res=c=0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c+=1
            res=max(res,c)
        else:c=0
    return res+1 if res else 0

print(valid( "leetcode"))