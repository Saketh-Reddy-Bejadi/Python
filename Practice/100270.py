s = "hello"
a=[]
r=0
for i in range(len(s)):
    a.append(ord(s[i]))
for i in range(len(a)):
    if i>0:
        r+=abs(a[i-1]-a[i])
print(r)