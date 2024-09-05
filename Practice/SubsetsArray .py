for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    res=[]
    i=0
    j=1
    while(i<n-1):
        if(j==n-1):
            res.append(arr[i:j+1])
            j=i+1
            i+=1
            
        res.append([arr[i:j]])
        j+=1

    for s in res:
        print(*s)
