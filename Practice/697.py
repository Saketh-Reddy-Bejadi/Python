nums =[1,2,2,3,1]
result={}
for n in nums:
    if n in result:
        result[n]+=1
    else:
        result[n]=1
m=max(result.values())
mostFreq=[]
for n,f in result.items():
    if f==m:
        mostFreq.append(n)
t=max(mostFreq)
r=0
for i in range(len(nums)-1,-1,-1):
    if nums[i]==t:
        r=i
        break
print(r)
    2347:: 