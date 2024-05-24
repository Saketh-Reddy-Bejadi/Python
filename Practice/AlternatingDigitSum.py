n=101
n=str(n)
s=0
for i in range(len(n)):
    e=int(n[i])
    if(i%2!=0):
        e=-e
    s+=e
print(s)