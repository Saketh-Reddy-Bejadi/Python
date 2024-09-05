def valid(nums):
    dic={}
    for n in nums:
        if n in dic:
            dic[n]+=1
        else:
            dic[n]=1
    for n in dic.keys():
        if dic[n]==1:
            return n
print(valid([1,1,2,3,3,4,4,8,8]))