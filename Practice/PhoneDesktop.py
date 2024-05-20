for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    ans += b // 2
    z = b // 2
    i = z
    while i > 0:
        a -= 7
        i -= 1
    a = max(0, a)
    if b % 2 == 1:
        a -= 11
        ans += 1
    a = max(0, a)
    ans += a // 15
    a -= 15 * (a // 15)
    if a > 0:
        ans += 1
    print(ans)