for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    totalSum=0
    count=0
    res=float('inf')
    for num in arr:
        totalSum+=abs(num)
        if num<0:
            count+=1
        res=min(res,abs(num))
    if count%2!=0:
        totalSum-=2*res
    print(totalSum)