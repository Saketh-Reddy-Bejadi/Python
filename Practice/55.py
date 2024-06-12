def Jump(nums):
    jump=1
    for i in nums[nums[0]:]:
        if jump==0:
            break::
        if jump>1:
            jump-=1
            continue
        else:
            jump=i
    return jump==nums[-1]
print(Jump([3,2,1,0,4]))