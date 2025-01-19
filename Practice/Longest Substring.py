def valid(s):
    d={}
    for c in s:
        if c in d:d[c]+=1
        else:d[c]=1
    p=[]
    a=''
    for c,n in sorted(d.items()):
        p.append(c*(n//2))
        if n%2==1 and (not a or c<a):a=c
    p=''.join(p)
    return p+a+p[::-1]

print(valid('abaccd'))