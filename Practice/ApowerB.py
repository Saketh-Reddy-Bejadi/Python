def power_mod(a, b, mod):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b //= 2
        print(b)
    return res

test_cases = int(input())
MOD = 1000000007

for _ in range(test_cases):
    a, b = map(int, input().split())
    result = power_mod(a, b, MOD)
    print(result)
