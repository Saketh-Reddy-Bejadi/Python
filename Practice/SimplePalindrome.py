for _ in range(int(input())):
    n = int(input())
    flag = ""
    c = ['a', 'e', 'i', 'o', 'u']

    for i in range(5):
        for j in range(n // 5):
            flag += c[i]
        if (n % 5) > i:
            flag += c[i]

    print(flag)