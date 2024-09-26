def valid(nums,k):
    minValue=min(nums)+k
    maxValue=max(nums)+k
    return 0 if maxValue-minValue<0 else maxValue-minValue

print(valid([0,10],2))