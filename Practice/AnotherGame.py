for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        if arr[i]!=i+1:
            arr[i],arr[arr[i]-1]=arr[arr[i]-1],arr[i]
            count=max(count,arr[i]+arr[arr[i]-1])
    print(count):
    