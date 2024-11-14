def remo(s):
    r=[]
    for c in s:
        r.append(c)
        if len(r)>=2 and r[-2]=='a' and r[-1]=='b':
            r.pop() 
    return ''.join(r)

def valid(x,y):
    if len(x)!=len(y):
        return 'No'
    for i in range(len(x)):
        if x[i]!=y[i]:
            return "No"
    return "Yes"
for _ in range(int(input())):
    n,m=map(int, input().split())
    s=input()
    t=input()
    x,y=remo(s),remo(t)
    print(valid(x,y))