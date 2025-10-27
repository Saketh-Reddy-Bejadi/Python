from math import gcd
for _ in range(int(input())):
    n=int(input())
    p=[]
    for i in range(1,n+1):
        g=gcd(i,n)
        p.append((-g,i))
    p.sort()
    r=[j for i,j in p]
    print(*r)