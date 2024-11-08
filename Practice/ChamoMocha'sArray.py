for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l,r=-1,10**9+1
    while l-r>1:
        mid=(l+r)//2
        m=c=p=0
        if a[0]>=mid: c=1
        else: c=-1
        for i in range(1,n):
            m=min(m,p)
            p=c
            if a[i]>=mid:c+=1
            else:c-=1
            if c-m>0:l=mid
            else: r=mid
    print(l)