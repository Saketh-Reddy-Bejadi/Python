s = "zbc"
t = "abc"
i=j=0
while(i<len(s) and j<len(t)):
    if s[i]==t[j]:
        t+=1
    s+=1
print(len(t)-j)