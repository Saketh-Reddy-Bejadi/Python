n=int(input())
arr=list(map(int,input().split()))
add=[]
sum=0
for num in arr:
    if num%2!=0:
        add.append(num)
for n in add:
    sum+=n
print(sum)