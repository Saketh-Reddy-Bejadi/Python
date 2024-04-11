t = int(input())
for _ in range(t):
    n = int(input())
    c2 = 0
    arr = list(map(int, input().split()))
    for e in arr:
        if e == 2:
            c2+= 1      
    if c2 % 8 == 0:
        print("Yes")
    else:
        print("No")