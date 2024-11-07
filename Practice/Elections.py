def valid(N, A, B, X):
    w=0
    a=[]
    for i in range(N):
        if(A[i]>B[i]):
            w+=1
        else:
            a.append(B[i]-A[i]+1)
    wt=(N//2)+1
    rw=wt-w
    if(rw<= 0):
        return True
    a.sort()
    vu=0
    for i in range(rw):
        vu+=a[i]
        if vu>X:
            return False 
    return True
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print("YES" if valid(n,a,b,x) else 'NO')