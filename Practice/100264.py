nums=[3,2,1]
Ic=Dc=0
res=0
for i in range(len(nums)):
    if nums[i-1]>nums[i]:
        Ic+=1
    elif nums[i-1]<nums[i]:
        Dc+=1
    else:
        res=max(res,Ic,Dc)
        Ic=Dc=1
print(max(res,Ic,Dc))