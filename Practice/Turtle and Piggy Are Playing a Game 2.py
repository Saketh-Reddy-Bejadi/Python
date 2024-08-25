for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    t=1
    i=0
    while(len(arr)!=1):
        if t%2!=0:
            ele=max(arr[i],arr[i+1])
            arr[i]=ele
            arr.remove(arr[i+1])
        else:
            ele=min(arr[i],arr[i+1])
            arr[i]=ele
            arr.remove(arr[i+1])
        t+=1
    for i in arr:
        print(i)