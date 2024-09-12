def valid(s):
    if len(s) == 0:
        return 0 
    Index = {}
    res = 0
    i = 0
    for j in range(len(s)):
        if s[j] in Index and Index[s[j]] >= i:
            i = Index[s[j]] + 1
        Index[s[j]] = j
        res = max(res, j - i + 1)
    return res

s = "dvdf"
print(valid(s))