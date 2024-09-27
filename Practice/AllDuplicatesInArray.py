def valid(nums):
    countArr={}
    res=set()
    for n in nums:
        if n in countArr:
            countArr[n]+=1
            res.add(n)
        else:
            countArr[n]=1
    return list(res)

print(valid([4,3,2,7,8,2,3,1]))