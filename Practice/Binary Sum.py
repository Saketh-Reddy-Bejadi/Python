for _ in range(int(input())):
    n,m=map(int,input().split())
    p=n//2 
    q=(n+1)//2
    if p<=m<=q:
        print('YES')
    else:
        print("NO")