for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    l=[0]*n
    r=[0]*n
    l[0]=arr[0]
    for i in range(1,n):
        l[i]=max(l[i-1],arr[i])
    r[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        r[i]=max(r[i+1],arr[i])
    w=0
    for i in range(n):
        w+=max(0,min(l[i],r[i])-arr[i])
    print(w)