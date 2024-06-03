num=1248
res=0
num=str(num)
for n in num:
    if int(num)%int(n)==0:
        res+=1
print(res)