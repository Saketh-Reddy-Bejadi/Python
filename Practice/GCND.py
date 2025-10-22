def gcnd(a):
    m=max(a)
    c=a.count(m)
    if(c>=2):return m-1
    for i in a:
        if(i!=m and i!=m-1):return m-1
    return m-2

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(gcnd(a))