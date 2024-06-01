nums =  [5,4,-1,7,8]
result=0
cSum=0
for i in range(len(nums)):
    cSum+=nums[i]
    result=max(result,cSum)
    if cSum<0:
        cSum=0
print(result)