for _ in range(int(input())):
    n,c=map(int,input().split())
    d=list(map(int,input().split()))
    t=list(map(int,input().split()))
    r=0
    for i in t:
        e=i-1
        if d[e]>0:
            d[e]-=1
        else:
            r+=1
    print(r)