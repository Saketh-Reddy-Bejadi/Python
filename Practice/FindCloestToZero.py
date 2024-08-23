def valid(nums):
    for i in range(len(nums)):
        nums[i]=0-nums[i]
    return min(nums)
    

nums = [-4,-2,1,4,8]
print(valid(nums))
