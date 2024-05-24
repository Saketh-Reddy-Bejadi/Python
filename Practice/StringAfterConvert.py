s = "zbax"
k = 2
t=""
for c in s:
    e=ord(c.lower())-ord('a')+1
    t+=str(e)
while(k>0):
    t=int(t)
    r=0
    while(t>0):
        r+=t%10
        t//=10
    t=r
    k-=1
print(r)