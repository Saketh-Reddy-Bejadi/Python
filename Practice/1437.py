def kLengthApart(nums,k):
    d=k
    for i in range(len(nums)):
        if nums[i]==0:
            d+=1
        else:
            if d<k:
                return False
            d=0
    return True
    
    
    
print(kLengthApart([1,0,0,0,1,0,0,1],2))
        