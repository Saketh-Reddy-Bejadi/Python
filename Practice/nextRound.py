# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
# count=0
# for i in range(n):
#     if arr[i]>0:
#         if arr[i]>=arr[k]:
#             count+=1
# if count>0:       
#     print(count)
# else:
#     print(0)



n, k = map(int, input().split())
scores = list(map(int, input().split()))
count = 0

for score in scores:
    if score > 0 and score >= scores[k - 1]:
        count += 1
    else:
        break
print(count)
