def Sum(arr):
    N=0
    for i in range(n-1):
        N+=abs(arr[i]-arr[i+1])
    return N
for _ in range(int(input())):
    n,e=map(int,input().split())
    A=list(map(int,input().split()))
    M=Sum(A)
    for i in range(n):
        O=A[i]   
        A[i]=1
        M=max(M,Sum(A))
        A[i]=e
        M=max(M,Sum(A))
        A[i]=O
    print(M)