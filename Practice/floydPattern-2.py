n=int(input())
start=1
for i in range(1,n+1):
    print(start,end=' ')
    for j in range(i-1):
        temp=start
        print(n+j-1,end=' ')
        temp+=1
    start+=1
    print() 