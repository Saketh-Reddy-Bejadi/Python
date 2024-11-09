def valid(s,k):
    sb=list(s)
    for i in range(0,len(sb),2*k):
        l=i
        r=min(i+k-1,len(sb)-1)
        while (l < r):
            sb[l]= s[r]
            sb[r]=s[l]
            l+=1
            r-=1
    print(s)
    return ''.join(sb)
s="abcdefg"
k=2
print(valid(s,k))