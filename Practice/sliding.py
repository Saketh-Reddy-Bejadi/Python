for _ in range(int(input())):
    n,m,a,b=map(int,input().split())
    r=0
    r+=m- b
    r+=(n-a)*(m-1)
    r+= (n-a)*m
    print(r)