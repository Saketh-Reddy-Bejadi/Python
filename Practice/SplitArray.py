def valid(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for val in dict.values():
        if val > 2:
            return False
    return True
print(valid([1,1,2,2,3,4]))
