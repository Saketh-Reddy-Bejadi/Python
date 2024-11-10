for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    d=[]
    x=0
    for i in range(n):
        if(a[i]>x):
            d.append(1)
            x+=1
        elif(a[i]==x):d.append(0)
        else:
            d.append(-1)
            x-=1
    xn=x
    minSum=d[0]
    cmin=d[0]
    nd=len(d)
    for i in range(1,nd):
        cmin=min(d[i],cmin+d[i])
        minSum=min(minSum,cmin)
    print(xn-minSum)
