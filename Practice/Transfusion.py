def valid(n,x):
    t=sum(x)
    o=sum(x[i] for i in range(n) if (i+1)%2!=0)
    e=sum(x[i] for i in range(n) if (i+1)%2==0)
    co=(n+1)//2
    ce=n//2
    if t%n!=0:return 'NO'
    t1=t//n
    if o==t1*co and e==t1*ce:return 'YES'
    else:return 'NO'
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    print(valid(n,x))