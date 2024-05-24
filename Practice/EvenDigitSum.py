num=30
c=0
for i in range(1,num+1):
    if len(str(i))>1:
        i=str(i)
        s=0
        for n in i:
            s+=int(n)
        i=s
    if(i%2==0):
        c+=1
print(c)