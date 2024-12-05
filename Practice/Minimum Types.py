for _ in range(int(input())):
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    coins=[(x[i]*y[i],i) for i in range(n)]
    coins.sort(reverse=True,key=lambda x:x[0])
    t=0
    s=0
    for v,i in coins:
        if s>=m:break
        m2=min(y[i],(m-s+x[i]-1)//x[i])
        s+=m2*x[i]
        t+=1
    print(t if s>=m else -1)