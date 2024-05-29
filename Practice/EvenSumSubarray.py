def evenSum(n,arr):
    for i in range(n):
            temp=0
            for j in range(i,n):
                temp+=arr[j]
                if temp%2==0:
                    return max(count,j-i+1)

for _ in range(int(input())):
    sizeOfArr=int(input())
    array=list(map(int,input().split()))
    count=0
    # for i in range(sizeOfArr):
    #     temp=0
    #     for j in range(i,sizeOfArr):
    #         temp+=array[j]
    #         if temp%2==0:
    #             count=max(count,j-i+1)
    print(evenSum)