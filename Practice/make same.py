for _ in range(int(input())):
    n=int(input())
    s=[]
    for i in range(3):
        r=input()
        s.append(r)
    c=[r.count('0') for r in s]
    z=sum(c)
    if(z%n)!=0:
        print(-1)
        continue
    k=z//n
    if k==0 or k==3:
        print(0)
        continue
    c=sorted(c,reverse=True)
    z=sum(c[:k])
    print(k*n-z)