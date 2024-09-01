def Valid(nums,k):
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    nums.sort()
    return str(nums[len(nums)-k])


print(Valid(["2","21","12","1"],3))