def ifThen(s,w):
    a={}
    for c in w:
        if c in s and c not in a:
            a[c]=1
        elif c in s and c in a:
            a[c]+=1
    return a
def valid(words):
    v={}
    for c in words[0]:
        if c in v:v[c]+=1
        else:v[c]=1
    for i in range(1,len(words)):
        a=ifThen(words[0],words[i])
        for c in v.keys():
            if c not in a.keys():
                v[c]=0
            elif v[c]>a[c]:
                v[c]=a[c]   
        v = {k: v for k, v in v.items() if v != 0}
    r=[]
    for k, v in v.items():
        for i in range(v):
            r.append(k)
    return r

words = ["cool","lock","cook"]
print(valid(words))