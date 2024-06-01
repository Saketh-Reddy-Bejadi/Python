nums = [1,2,2,3,1]
result={}
for n in nums:
    if n in result:
        result[n]+=1
    else:
        result[n]=1
m=max(result,key=result.get)
r=0
for i in range(len(nums)):
    if nums[i]==m:
        r=i
print(r-(nums.index(m)))::