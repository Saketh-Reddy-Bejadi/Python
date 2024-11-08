def mincost(N, A):
    tc = 0
    for i in range(N):
        mc = float('inf')
        for j in range(3):
            c = abs(A[i] - j)
            if c < mc:
                mc = c
        tc += mc
    return tc

N = int(input())
A = list(map(int, input().split()))

print(mincost(N, A))
