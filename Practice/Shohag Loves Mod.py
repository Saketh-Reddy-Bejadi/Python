for t in range(int(input())):
    n=int(input())
    res=[]
    
    for i in range(1,n+1):
        res.append(i*2-1)
    print(*res)