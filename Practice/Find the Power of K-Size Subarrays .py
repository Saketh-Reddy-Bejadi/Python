def valid(nums,k):
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        sub = nums[i:i + k]
        if isvalid(sub):
            res.append(max(sub))
        else:
            res.append(-1)
    
    return res
def isvalid(arr):
    n = len(arr)
    if n <= 1:
        return True
    for j in range(1, n):
        if arr[j] != arr[j-1] + 1:
            return False
    return True
nums = [3,2,3,2,3,2]
k = 2
print(valid(nums,k))