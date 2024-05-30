x=input()
temp=x.split()
s=temp[0]
t=temp[1]
i=0
j=len(s)-len(t)
c=0
while(i<len(t)):
    if s[i]==t[i] and s[j]==t[i]:
        c+=1
    i+=1
    j+=1
    
if c==len(t):
    print("Yes")
else:
    print("No")
