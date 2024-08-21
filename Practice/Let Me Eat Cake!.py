for _ in range(int(input())):
    a, b = map(int, input().split())
    res = 0
    while a != b:
        if a > b:
            toEat = (a + 1) // 2
            res += toEat
            a -= toEat
        else:
            toEat = (b + 1) // 2
            res += toEat
            b -= toEat
    print(res)
