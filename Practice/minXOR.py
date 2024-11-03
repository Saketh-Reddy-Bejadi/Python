def valid(arr,n,k):
    r=0
    for i in arr:
        r^=i
    if r==0:
        return 0
    op=k
    for b in range(31,-1,-1):
        if op==0:
            break
        c=sum((i>>b)&1 for i in arr)
        if c>0 and ((r>>b)&1)==1:
            for i in range(n):
                if (arr[i]>>b)&1:
                    arr[i]^=(1<<b)
            r=0
            for j in arr:
                r^=j
            op-=1
    return r
arr=[1,2,5,7,9,6]
n=6
k=2
print(valid(arr,n,k))