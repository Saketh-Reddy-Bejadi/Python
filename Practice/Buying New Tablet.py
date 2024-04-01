t=int(input())
for _ in range(t):
    n,co=map(int,input().split())
    ar=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        if c<=co:
            ar.append(a*b)
    print(max(ar))
