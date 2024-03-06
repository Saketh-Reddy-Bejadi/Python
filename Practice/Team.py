n=int(input())
count=0
for _ in range(n):
    arr=list(map(int,input().split()))
    if arr.count(1)>1:
        count+=1
print(count)