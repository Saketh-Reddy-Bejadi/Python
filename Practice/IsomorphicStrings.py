def valid(s,t):
    if len(s) != len(t):
            return False
    ST = {}
    TS = {}
    for i in range(len(s)):
        if s[i] in ST:
            if ST[s[i]] != t[i]:
                return False
        else:
            ST[s[i]] = t[i]
            
        if t[i] in TS:
            if TS[t[i]] != s[i]:
                return False
        else:
            TS[t[i]] = s[i]
    return True
            
            
print(valid('foo','bar'))