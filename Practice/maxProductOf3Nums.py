import math
def valid(nums):
    if len(nums)==3:
        return math.prod(nums)
    nums.sort()
    return max((nums[0]*nums[1]*nums[-1]),math.prod(nums[len(nums)-3:]))
    

nums =[-100,-98,-1,2,3,4]
print(valid(nums))