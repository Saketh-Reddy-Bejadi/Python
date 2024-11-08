def valid(n, a):
    a.sort() 
    mex = 0

    for i in range(n):
        if i % 2 == 0: 
            if a[i] == mex:
                mex += 1

    return mex

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(valid(n, a))
