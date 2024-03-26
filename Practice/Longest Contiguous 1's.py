n=int(input())
arr=list(map(int,input().split()))
m=0
c=0
for num in arr:
    if num==1:
        c+=1
    else:
        c=0
    m=max(m,c)
print(m)