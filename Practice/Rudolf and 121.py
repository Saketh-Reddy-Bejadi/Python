def zero(arr, n):
    o = [0] * n

    for i in range(1, n - 1):
        o[i] = max(0, arr[i] - arr[i - 1])

    for i in range(1, n - 1):
        if arr[i] < o[i]:
            return "NO"
        arr[i] -= o[i]
        arr[i + 1] -= o[i]
        o[i + 1] += o[i] * 2

    return "YES" if all(x == 0 for x in arr) else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(zero(arr, n))
