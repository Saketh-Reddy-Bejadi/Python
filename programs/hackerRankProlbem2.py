# def compareTriplets(a, b):
#     res=[0,0]
#     for i in range(0,len(a)):
#         if a[i]>b[i]:
#             res[0]=res[0]+1
#         if a[i]<b[i]:
#             res[1]=res[1]+1
#     return res
# a = list(map(int, input().rstrip().split()))
# b = list(map(int, input().rstrip().split()))
# result = compareTriplets(a, b)
# print(result)



n = int(input())
arr = list(map(int, input().split()))
arr.pop(max(arr))
print(max(arr))
    