for _ in range(int(input())):
    n = int(input())
    s = input()
    res = "NO"
    for i in range(n - 1):
        if s[i] != s[i - 1]:
            res = "YES"
    if s[0] == s[-1]:
        res = "NO"
    print(*res)
