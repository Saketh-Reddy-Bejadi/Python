def Jump(nums):
    if len(nums)==1:return True
    jump=0
    for step in nums:
        if jump<0:
            return False
        elif step>jump:
            jump=step
        jump-=1
    return True
print(Jump([3,2,1,0,4]))