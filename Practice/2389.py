nums = [4,5,2,1]
queries = [3,10,21]
nums.sort()
res=[]
c=0
s=0
for i in range(len(queries)):
    c=0
    s=0
    for j in range(len(nums)):
        if s+nums[j]<=queries[i]:
            s+=nums[j]
            c+=1
        else:
            break
    res.append(c)
print(res)