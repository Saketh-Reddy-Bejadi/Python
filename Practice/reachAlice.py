def numWays(s):
    a=10**9+7
    b=len(s)
    c=[0]*(b+1)
    c[1]=1
    for i in range(1,b+1):
        if (i+1)<=b:
            c[i+1]=(c[i+1]+c[i])%a
        if (i+2<=b) and (s[i-1]=='0'):
            c[i+2]=(c[i+2]+c[i])
    return c[b]

s='1010'
print(numWays(s))