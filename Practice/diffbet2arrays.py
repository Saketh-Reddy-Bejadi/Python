def findDifference(nums1,nums2):
    a=sorted(list(set(nums1)))
    b=sorted(list(set(nums2)))
    for i in nums1:
        if i in b:
            a.remove(i)
            b.remove(i)
    return [a,b]
    
findDifference([1,2,3,4,5],[1,2,4,5,6])