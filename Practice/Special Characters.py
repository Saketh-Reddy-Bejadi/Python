def solve(n):
    if n == 1:
        return "NO"
    if n == 2:
        return "YES\nMM"
    if n == 6:
        return "YES\nAAABAACC"
    if n % 2 == 0:
        return "YES\n" + "AB" * (n // 2)
    return "NO"

t = int(input())
for _ in range(t):
    n=int(input())
    print(solve(n))