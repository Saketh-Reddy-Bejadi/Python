nums = [3,1,2,4]
el=sorted([nums[i] for i in range(len(nums)) if nums[i]%2==0])
ol=sorted([nums[i] for i in range(len(nums)) if nums[i]%2!=0])
print(el+ol)
