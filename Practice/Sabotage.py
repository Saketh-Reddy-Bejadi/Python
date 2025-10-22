for _ in range(int(input())):
    x,y,z=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    for i in range(min(z,x)):
        if(l[i]>y):
            y+=100
            l[i]=0 
        else:break 
    a=sum(1 for e in l if e>y)
    print(a+1)
    