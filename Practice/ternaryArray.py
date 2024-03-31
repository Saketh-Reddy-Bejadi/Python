n=int(input())
a=list(map(int,input().split()))
tc=0
for i in range(len(a)):
    if a[i]<0:
        a[i]=abs(a[i]-0)
    elif a[i]==0:
        a[i]=abs(a[i]-1)
    elif a[i]>2:
        a[i]=abs(a[i]-2)
    elif a[i]==1:
        a[i]=abs(a[i]-1)
print(sum(a))