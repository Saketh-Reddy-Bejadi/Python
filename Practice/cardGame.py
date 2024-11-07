for _ in range(int(input())):
    n,x=map(int,input().split())
    ec=n//2
    oc=(n+1)//2
    
    if x%2==0:
        print(ec-1)
    else:
        print(oc-1)