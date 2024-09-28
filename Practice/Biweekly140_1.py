def valid(nums):
    for i in range(len(nums)):
        ele=0
        while(nums[i]):
            ele+=nums[i]%10
            nums[i]=nums[i]//10
        nums[i]=ele
    return min(nums)
    
print(valid([999,19,199]))