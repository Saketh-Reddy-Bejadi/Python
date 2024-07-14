def valid(nums):
    n,res=len(nums),0
    for i in range(n):
        print("e",nums[i])
        if n%(i+1)==0:
            res+=nums[i]**2
    return res
nums = [1,2,3,4]
print(valid(nums))