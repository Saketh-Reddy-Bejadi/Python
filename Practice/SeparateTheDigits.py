nums = [13,25,83,77]
r=[]
for i,n in enumerate(nums):
    n=str(n)
    for i in range(len(n)):
        r.append(int(n[i]))
    
print(r)