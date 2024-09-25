for _ in range(int(input())):
    n=int(input())
    temp=[0]*(n+1)
    for i in range(n-1):
        u,v=map(int,input().split())
        temp[u]+=1
        temp[v]+=1
    res=temp.count(1)
    count=n-res
    print(res*3+count*2)