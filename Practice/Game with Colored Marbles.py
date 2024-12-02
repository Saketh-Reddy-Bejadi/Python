def solve(l):
    d1,d2={},{}
    for i in range(len(l)):
        d1[l[i]]=d1.get(l[i],0)+1
    l.sort()
    for k,v in d1.items():
        if v not in d2:
            d2[v]=[]
        d2[v].append(k)
    a=0
    for i,j in d2.items():
        if i==1:
            t=(len(j)//2)+(len(j)%2)
            a+=(t*2)
        else:
            a+=len(j)
    return a
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(solve(l))