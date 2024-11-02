for _ in range(int(input())):
    m,n=map(int,input().split())
    d={}
    for i in range(n):
        b,c=map(int,input().split())
        if(b in d):d[b]+=c
        else:d[b]=c
    d=sorted(d.values(),reverse=True)

    print(sum(d[:m]))