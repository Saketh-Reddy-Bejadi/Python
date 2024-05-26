nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
res=[]
count=0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]%(nums2[j]*k)==0:
            count+=1
            res.append((i,j))
print(count)
print(res)