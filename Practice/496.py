def valid(n2,n):
    for j in range(n2.index(n),len(n2)):
        if n2[j]>n:
            return n2[j]
    return -1
nums1 = [2,4]
nums2 = [1,2,3,4]
res=[]
for i,n in enumerate(nums1):
    if n in nums2:
        res.append(valid(nums2,n))
print(res)