nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
indices=[]
for i in range(len(nums)):
    if nums[i]==x:
        indices.append(i)
ans=[]
for oc in queries:
    if oc-1<len(indices):
        ans.append(indices[oc-1])
    else:
        ans.append(-1)
print(ans)
