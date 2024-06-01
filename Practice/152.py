nums = [3,-1,4]
res=float("-inf")
cPro=1
for i in nums:
    cPro*=i
    res=max(res,cPro)
    if cPro==0:
        cPro=1
print(res)