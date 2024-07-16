def valid(v,N,X):
    res=[]
    for i in range(N):
        if v[i]==X:
            res.append(i)
    if res:
        return res[0],res[-1]
    else:
        return -1, -1

N = 9
v = [1, 3, 5, 5, 5, 5, 67, 123, 125]
X = 5
ans=valid(v,N,X)
if ans[0]==-1:
    print(-1)
else:
    print(ans[0], ans[1])