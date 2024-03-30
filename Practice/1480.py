nums=[1,2,3,4]
s=0
for i in range(len(nums)):
    s+=nums[i]
    nums[i]=s
print(nums)