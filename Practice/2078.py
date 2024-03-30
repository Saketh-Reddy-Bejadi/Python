colors=[1,8,3,8,3]
n=len(colors)
m=l=r=0
for i in range(len(colors)):
    if colors[i]!=colors[0]:
        l=i
    elif colors[i]!=colors[n-1]:
        r=n-i-1
    else :
        m=0
    m=max(m,l,r)
print(m)


