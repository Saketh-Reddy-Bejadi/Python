import math
nums = [1,2,3,4]
res=[0]*len(nums)
for i in range(len(nums)):
    res[i]=math.prod(nums[i+1:])*math.prod(nums[:i])
print(res)
