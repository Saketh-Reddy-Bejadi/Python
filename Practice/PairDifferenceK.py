for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    res=False
    arr.sort()
    i=0
    j=n-1
    while(i<j):
        if(arr[j]-arr[i]==k):
            res=True
            break
        elif(arr[j]-arr[i]<k):
            j-=1
        elif(arr[j]-arr[i]>k):
            i+=1
    print(res)