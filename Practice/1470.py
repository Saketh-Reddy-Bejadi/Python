nums=[2,5,1,3,4,7] 
n=3
j=0
for i in range(len(nums)):
    if i%2!=0 and i<n//2 :
        nums[i]=nums[n+j]
        nums[i+1]=nums[i]
        j+=1
print(nums)