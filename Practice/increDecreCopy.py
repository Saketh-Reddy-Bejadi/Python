def oper(A,B,n):
    t=0
    m=float('inf')
    l=B[n]
    r=False
    for i in range(n):
        t+=abs(A[i]-B[i])
        if (l>=A[i] and l<=B[i]) or (l>=B[i] and l<=A[i]):
            r=True
        m=min(abs(l-A[i]),abs(B[i]-l),m)
    return r,t,m
    
    
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    r,t,m=oper(A,B,n)
    if r:
        print(t+1)
    else:
        print(t+m+1)