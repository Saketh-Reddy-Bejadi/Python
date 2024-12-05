def flor(a,b):
    if b==0:return 0
    if a>=0:return a//b
    else:
        if a%b==0:return a//b
        else:return (a//b)-1
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    c=0
    for i in a:
        if i>=0:f=i//k
        else:f=(i-(k-1))//k
        s+=f
        m=i%k
        if m<0:m+=k
        if m!=0:c+=1
    if s<=0<=(s+c):print('YES')
    else:print('NO')
