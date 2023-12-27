def countCandy(A):
    N = len(A)
    rc = [False] * N
    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[j] < A[i]:
                rc[j] = True 
    return sum(rc)

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    r = countCandy(A)
    print(r)
