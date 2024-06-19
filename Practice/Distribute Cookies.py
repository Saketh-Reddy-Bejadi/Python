for _ in range(int(input())):
    n,m=map(int,input().split())
    if m<n:
        print(n-m)
    else:
        inc=n-(m%n)
        dec=m%n
        print(min(inc,dec))