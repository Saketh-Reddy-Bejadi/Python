def twoSum(nums,target):
    res=[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]!=nums[j] and nums[i]+nums[j]==target and i not in res and j not in res:
                res.append(i)
                res.append(j)
            else:
                continue
    print(res)
twoSum([3,2,4],6)