
nums = [0,1,2,4,5,7]
res=[]
temp=set()
nums=nums[::-1]
for i in range(len(nums)-1,-1,-1):
    if nums[i-1]==nums[i]+1:
        temp.add(nums[i]) 
        temp.add(nums[i-1])
    else:
        res.append(str(min(temp))+"->"+str(max(temp)))
        temp=set()
print(res)