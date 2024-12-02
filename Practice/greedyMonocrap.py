def valid(a,k):
    s=0
    for e in a:
        s+=e
        if s>k:
            s-=e
            print(k-s)
            return
    print(k-s)
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    valid(a,k)