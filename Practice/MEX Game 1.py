def alice_score(n, a):
    a.sort()  # Sorting in non-decreasing order
    mex = 0

    for i in range(n):
        if i % 2 == 0:  # Alice's turn
            if a[i] == mex:
                mex += 1

    return mex

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(alice_score(n, a))
