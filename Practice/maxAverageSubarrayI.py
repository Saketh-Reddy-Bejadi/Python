def findMaxAverage(nums,k):
    n=len(nums)
    if n<=4:
        return sum(nums)/k
    a=sum(nums[:k])
    r=a
    i=k
    while i<n:
        a+=nums[i]-nums[i-k]
        r=max(r,a)
    return r/k

nums=[1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
