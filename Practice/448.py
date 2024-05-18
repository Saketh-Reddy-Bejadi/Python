nums = [1,1]
l=len(nums)
nums.sort()
nums=list(set(nums))
i=1
res=[]
j=0
while(len(res)+j<l+1):
    if nums[j]!=i:
        res.append(i)
    i+=1
    j+=1
print(res)