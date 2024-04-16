def twoSum(nums,target):
    res=set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]!=nums[j] and nums[i]+nums[j]==target:
                res.add(i)
                res.add(j)
            else:
                continue
    res=list(res)
    print(res)
twoSum([3,2,4],6)