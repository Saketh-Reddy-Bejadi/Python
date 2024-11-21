for _ in range(int(input())):
    m=int(input())
    o=list(map(int,input().split()))
    u=0
    for i in range(m):
        if o[i]==i+1:
            u+=1
    if(u==m):
        print(m)
    elif(u>=1):
        print(m-1)
    else:
        if(m>=2):
            print(m-2)
        else:
            print(0)
