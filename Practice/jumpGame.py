def valid(nums):
    if len(nums)==1:return True
    jump=0
    for step in nums:
        if jump<0:
            return False
        elif step>jump:
            jump=step
        jump-=1
    return True


print(valid([2,5,0,0]))