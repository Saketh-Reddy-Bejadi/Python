def valid(p,b):
    w=''
    for c in p:
        if c.isalpha() or c.isspace():
            w+=c.lower()
        else:
            w+=' '
    p=w
    print(p)
    w = p.split()
    c={}
    for i in w:
        if i not in b:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
    c=0
    res=''
    for i in c.keys():
        if c[i]>c:
            c=c[i]
            res=i
    return res
    



p ="a, a, a, a, b,b,b,c, c"
b = ["a"]
print(valid(p,b))