def valid(nums):
    # t=list(set(nums))
    # nums.sort()
    # t.sort()
    # if t==nums:
    #     return False
    # return True
    num_set = set()
    for n in nums:
        if n in num_set:
            return True
        num_set.add(n)
    return False
nums=[1,5,-2,-4,1]
print(valid(nums))
