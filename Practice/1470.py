nums=[2,5,1,3,4,7] 
n=3
res=[]
for i in range(1,len(nums)):
    if i%2==0:
        res.append(nums[i//2])
    else:
        res.append(nums[n+i//2])
print(res)