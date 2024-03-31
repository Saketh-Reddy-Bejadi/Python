a=[1,1,0,1,0]
# m=max(a)
# for i in range(len(a)):
#     if a[i]>m:
#         a.append(a[i])
#         a.remove(a[i])
#     else:
#         a.append(m)
#         a.remove(m)
# print(a)

s=0
e=len(a)-1
while(s!=e):
    if a[s]>a[e]:
        a[s],a[e]=a[e],a[s]
        s+1
        e-=1
    elif a[s]==a[e]:
        e-=1
print(a)