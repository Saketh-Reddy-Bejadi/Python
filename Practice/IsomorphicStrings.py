def valid(s,t):
    if len(s)!=len(t):
        return False
    # sCount={}
    # tCount={}
    # for c in s:
    #     if c in sCount:
    #         sCount[c]+=1
    #     else:
    #         sCount[c]=1
    # for c in t:
    #     if c in tCount:
    #         tCount[c]+=1
    #     else:
    #         tCount[c]=1
    # for i,j in sCount.
    for i in range(len(s)):
        if s.count(s[i])!=t.count(t[i]):
            return False
    return True

print(valid('foo','bar'))