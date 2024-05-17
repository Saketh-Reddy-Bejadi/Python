t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    if (sum(a)%2!=0):
        print(-1)
    else:
        n=a[0]+a[1]
        print(min(sum(a)//2,n))