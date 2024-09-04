
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(k):
        minV=arr.pop(0)
        maxV=arr.pop(-1)
        newValue=minV+maxV
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] < newValue:
                l = m + 1
            else:
                r = m
        arr.insert(l, newValue)
    print(arr)
