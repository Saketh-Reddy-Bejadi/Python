e=[5,2,-10,-5,1]
k=3
r=-1
i=0
x=i+k
while(i<len(e)):
    n=i
    t=0
    while(n<=len(e)-1):
        t+=e[i]
        n+=k
    r=r if r>t else t
    i+=1
r=r if r>0 else -1
print(r)