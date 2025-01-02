for _ in range(int(input())):
    n=int(input())
    s=input()
    oc,zc=0,0
    for i in s:
        if i=='1': oc+=1
        else: zc+=1
    if oc==n or zc==n:print(n)
    else:print(1)