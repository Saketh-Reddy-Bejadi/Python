nums = [1,2,3,4]
res=[1]*len(nums)
c=1
for i in range(len(nums)) :
    res[i] *= c
    c *= nums[i]
c=1
for i in range(len(nums)-1,-1,-1):
    res[i] *= c
    c *= nums[i]
print(res) 