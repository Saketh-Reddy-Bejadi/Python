# def valid(s,w):
#     n=len(s)
#     p=''
#     r=0
#     i=0
#     while i<n:
#         if s[i]!=p:
#              p=s[i]
#              i+=1
#         else:
#             j=i-1
#             a=[]
#             while(p==s[j]):
#                 a.append(w[j])
#                 p=s[j]
#                 j+=1
#             i=j
#             a.remove(max(a))
#             r+=sum(a)
#     return r
            
s=input().strip()
w=list(map(int,input().split()))
n=len(s)
a=int(s[0])
b=w[0]
r=0
for i in range(1,n):
    if int(s[i])==a:
        r+=min(b,w[i])
        b=max(b,w[i])
    else:
        a=int(s[i])
        b=w[i]
print(r)
