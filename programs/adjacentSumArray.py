def adja(b,n):
    b.sort()
    for i in range(1,b[-1]+1):
        A=[i]
        f=True
        for j in range(n-1):
            t=b[j]-A[-1]
            if t<=0:
                f=False
                break
            A.append(t)
        B=[A[j]+A[j+1] for j in range(len(A)-1)]
        B.sort()
        if B==b:
            print(*A)
            break
for _ in range(int(input())):
    n=int(input())
    B=list(map(int,input().split()))
    adja(B,n)