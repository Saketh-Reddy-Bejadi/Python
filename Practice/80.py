nums = [0,0,1,1,1,1,2,3,3]
start,end=0,0
while(end<len(nums)):
    count=1
    while(end+1<len(nums) and nums[end]==nums[end+1]):
        end+=1
        count+=1
    for i in range(min(2,count)):
        nums[start]=nums[end]
        start+=1
    end+=1
print(start)