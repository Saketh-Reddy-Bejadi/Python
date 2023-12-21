n=int(input()) 
arr=list(map(int,input().split()))
for num in arr:
    if arr.count(num)>1:
        print(num)