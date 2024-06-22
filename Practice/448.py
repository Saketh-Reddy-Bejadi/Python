nums = [4,3,2,7,8,2,3,1]
n=len(nums)
s=set(range(1,n+1))
print(list(s - set(nums)))