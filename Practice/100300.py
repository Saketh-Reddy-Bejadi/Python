from collections import Counter
nums=[13,23,12]
nl=len(str(nums[0]))
tc=len(nums)
dc=[]
for _ in range(nl):
    dc.append(Counter())
for i in nums:
    sn=str(i)
    for j in range(nl):
        dc[j][sn[j]]+=1
td=0
for i in range(nl):
    for d in dc[i]:
        c=dc[i][d]
        for d1 in dc[i]:
            if d!=d1:
                c1=dc[i][d1]
                td+=c*c1
print(td//2)