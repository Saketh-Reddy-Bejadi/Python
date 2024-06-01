
def reverse(s):
    sList = list(s)
    c='aeiouAEIOU'
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and sList[i] not in c:
            i += 1
            
        while i < j and sList[j] not in c:
            j -= 1
            
        if i < j:
            sList[i], sList[j] = sList[j], sList[i]
            i += 1
            j -= 1    
    return ''.join(sList)


s = "leetcode"
print(reverse(s))