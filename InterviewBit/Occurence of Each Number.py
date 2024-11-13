def findOccurences(A):
    A.sort()
    d={}
    for e in A:
        if e in d:
            d[e]+=1
        else:
            d[e]=1
    res=[e for e in d.values()]
    return res


A=[1, 2, 3]
print(findOccurences(A))

