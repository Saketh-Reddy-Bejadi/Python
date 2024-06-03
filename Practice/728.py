def dividing(n):
    t=str(n)
    if '0' in t:
        return False
    else:
        l=len(t)
        while(l):
            t=int(t)
            d=t%10
            if n%d!=0:
                return False
            t/=10
            l-=1
    return True
left = 47
right = 85
res=[]
for i in range(left,right+1):
    if (dividing(i)):
        res.append(i)
print(res)
