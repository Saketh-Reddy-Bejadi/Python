for _ in range(int(input())):
    l=int(input())
    s=list(map(int,input().split()))
    o=sum(s)
    print(o%2,min(o,2*l-o))