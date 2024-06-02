s = "abcdefgh"
s=list(s)
n=len(s)
k = 2
i=0
while(i<len(s)-1):
    if n>k:
        s[i],s[i+1]=s[i+1],s[i]
        n-=4
        i=(i+k)*2
    else:
        t=s[i:]
        t.reverse()
        s=s[:i-1]+t
print(s)::