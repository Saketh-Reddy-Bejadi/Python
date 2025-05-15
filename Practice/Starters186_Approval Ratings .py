for _ in range(int(input())):
    arr=list(map(int,input().split()))
    arr.sort()
    c=0
    s=sum(arr)
    i=0
    while(s<35):
        s+=(10-arr[i])
        c+=100
        i+=1
    print(c)