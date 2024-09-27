def valid(nums):
    res=set()
    for i in nums:
        if nums.count(i)>1:
            res.add(i)
    return list(res)
    
print(valid([0,1,1,0]))