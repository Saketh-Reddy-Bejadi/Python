n=int(input())
arr=list(map(int,input().split()))
unq=[]
for ele in arr :
    if ele not in unq:
        unq.append(ele)
for i in range(len(unq)) :
    print(unq[i],end=" ")