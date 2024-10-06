from itertools import permutations
def max_binary_concatenation(nums):
    binaryStrings = [bin(num)[2:] for num in nums]
    maxValue = 0
    for p in permutations(binaryStrings):
        concatBin = ''.join(p)
        currVal = int(concatBin, 2)        
        if currVal > maxValue:
            maxValue = currVal
    return maxValue
nums = [2,8,16]
result = max_binary_concatenation(nums)
print(result)
