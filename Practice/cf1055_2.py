def evalFunc(n,a,b,c,d,s):
    e=max(0,a-s)
    f=min(n,a+s)
    g=max(0,b-s)
    h=min(n,b+s)
    x=max(abs(e-c),abs(f-c))
    y=max(abs(g-d),abs(h-d))
    return max(x,y)

for _ in range(int(input())):
    n,a,b,c,d=map(int,input().split())
    l=0
    h=max(max(c,n-c),max(d,n-d))
    while l<h:
        m=(l+h)//2
        if evalFunc(n,a,b,c,d,m)>=m+1:l=m+1
        else:h=m
    print(l)