t=int(input())
for _ in range(t):
    c=neg=0
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        if i<=r and i>=l:
            c+=1
        else:
            c-=1
            neg+=1
    print(c,-neg)