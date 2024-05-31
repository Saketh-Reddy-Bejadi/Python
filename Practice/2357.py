nums = [1,5,0,3,5]
c=0
while(set(nums)!={0}):
    nums=list(set(nums))
    nums.sort()
    if len(nums)>1:
        x=nums[1]
    else:
        x=nums[0]
    for i in range(len(nums)):
        nums[i]-=x
        if nums[i]<0:
            nums[i]=0
    c+=1
print(c)
2357:::
