for _ in range(int(input())):
    u=int(input())
    a=list(map(int,input().split()))
    c=a[0]
    a.sort()
    if(c==a[0]):
        print(c+(a[1]-c)//2)
    elif c==a[-1]:
        print((10**6)-c+1+(c-a[-2])//2)
    else:
        l,u=0,0
        for i in range(len(a)):
            if(a[i]==c):
                l=(c-(c-a[i-1])//2)
                u=(c+(a[i+1]-c)//2)
                break
        print(u-l+1)

