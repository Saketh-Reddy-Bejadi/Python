n=int(input())
s=input().split()
v='aeiouAEIOU'
c=[]
for w in s:
    if w[0] in v and w[-1] in v:
        c.append(1)
    else:
        c.append(0)
p=[0]*(n+1)
for i in range(n):
    p[i+1]=p[i]+c[i]
for _ in range(int(input())):
    x,y=map(int,input().split())
    r=p[y+1]-p[x]
    print(r)