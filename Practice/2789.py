nums = [5,3,3]
n=len(nums)
i=0
while(nums!=sorted(nums,reverse=True)):
    if(i==n-1):
        i=0
    if nums[i]<=nums[i+1]:
        nums[i+1]+=nums[i]
        nums.remove(nums[i])
        n-=1
        i+=1
print(max(nums))
