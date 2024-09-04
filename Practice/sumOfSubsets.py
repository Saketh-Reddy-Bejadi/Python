for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    res=False
    arr.sort()
    i=0
    j=n-1
    while(i<j):
        if(arr[i]+arr[j]==k):
            res=True
            break
        elif(arr[i]+arr[j]>k):
            j-=1
        elif(arr[i]+arr[j]<k):
            i+=1
    print(res)