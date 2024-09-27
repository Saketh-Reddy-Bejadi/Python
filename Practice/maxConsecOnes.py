def valid(nums):
    res=c=0
    for n in nums:
        if n==1:
            c+=1
            res=max(res,c)
        else:c=0
    return res
         
print(valid([1,0,1,1,0,1]))