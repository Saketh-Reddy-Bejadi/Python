t=int(input())
for _ in range(t):
    n=int(input())
    for _ in range(n):
        str=input()
        for r in str:
            if r=='R':
                print('P',end="")
            if r=='P':
                print('S',end="")
            if r=='S':
                print('R')