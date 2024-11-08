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
s = list(map(int, input().split()))
c = 0

for i in s:
    if i > 0 and i >= s[k - 1]:
        c += 1
    else:
        break
print(c)
