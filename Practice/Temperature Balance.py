for _ in range(int(input())):
    a=int(input())
    z=list(map(int,input().split()))
    c,y=0,0
    for i in range(a):
        c+=z[i]
        y+=abs(c)
    print(y)