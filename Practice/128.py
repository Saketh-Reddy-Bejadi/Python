nums = [0,3,7,2,5,8,4,6,0,1]
numSet=set(nums)
res=0
for n in nums:
    if n- 1 not in nums:
        num = n
        c= 1
    while(num+1 in nums):
        num+=1
        c+=1
    res=max(res,c)
print(res)