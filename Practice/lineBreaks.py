def valid(s,m):
    l=0
    c=0
    for i in s:
        w=len(i)
        if l+w<=m:
            l+=w
            c+=1
        else:break 
    return c

for _ in range(int(input())):
    n,m=map(int,input().split())
    s=[input() for i in range(n)]
    print(valid(s, m))
