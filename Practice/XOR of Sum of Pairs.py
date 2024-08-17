for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    res=1
    for i in range(n):
        for j in range(i,n):
            res^=arr[j]
        res!=arr[i]
    print(res)