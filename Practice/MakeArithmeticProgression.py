for _ in range(int(input())):
    x, y, z = map(int, input().split())
    count = 0
    if not ((y - x) == (z - y)):
        count += 1
    print(count)
