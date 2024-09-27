def valid(nums):
    SingleDigitSum=DoubleDigitSum=0
    for n in nums:
        if n > 9:DoubleDigitSum+=n
        else:SingleDigitSum+=n
    return SingleDigitSum != DoubleDigitSum
    
print(valid([5,5,5,25]))