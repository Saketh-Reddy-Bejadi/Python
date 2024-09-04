def valid(arr,n,k):
    for i in range(k):
            miv=arr.pop(0)
            mav=arr.pop(-1)
            e=miv+mav
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < e:
                    l = m + 1
                else:
                    r = m
            arr.insert(l, e)
    return arr
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(*valid(arr,n,k))
