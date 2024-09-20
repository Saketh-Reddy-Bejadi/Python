for _ in range(int(input())):
    n = int(input())
    xVar, yVar = map(int, input().split())
    if xVar >= yVar:
        res = n // yVar + (n % yVar > 0)
    else:
        res = n // xVar + (n % xVar > 0)
    print(res)
