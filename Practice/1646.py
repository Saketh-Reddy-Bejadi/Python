import math
n = 7
nums=[0]*(n+2)
nums[1]=1
i=2
j=1
while(i<math.ceil((n+1)/2)+1):
    nums[j*2]=nums[j]
    nums[(j*2)+1]=nums[j]+nums[i]
    i+=1
    j+=1
print(max(nums[:n+1]))
