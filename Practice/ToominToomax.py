def maxexp(arr):
    arr.sort()
    return 2*(arr[-1]-arr[0])
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxexp(arr))