def isSorted(a):
    d={}
    for i in range(len(a)):
        b=setBits(a[i])
        if(b not in d):d[b]=[]
        d[b].append(i)

    for i in d.values():
        v=[a[idx] for idx in i]
        v.sort()
        for i,j in enumerate(i):a[j]=v[i]
    for i in range(1, len(a)):
        if(a[i]<a[i-1]):return False
    return True
def setBits(i):
    r=0
    while i:
        r+=(i&1)
        i>>=1
    return r
t=int(input())
for _ in range(t):
    l=int(input())
    a=list(map(int,input().split()))
    if isSorted(a):print("Yes")
    else:print("No")

