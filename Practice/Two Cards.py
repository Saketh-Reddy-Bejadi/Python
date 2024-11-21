for _ in range(int(input())):
    l=int(input())
    d=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m,n=0,-1
    for i in range(l):
        c=max(d[i],b[i])
        if c>m:
            m=c
            n=i
    w,x,y,z=0,-1,0,-1
    for i in range(l-1,-1,-1):
        if d[i]>w:
            y,z,w,x=w,x,d[i],i
        elif d[i]>y:
            y=d[i]
            z=i
    w=max(d[x],b[x])
    y=max(d[z],b[z])
    if w==y and m==w:
        print('No')
    else:
        print('Yes')