def find_array(n,k,ops):
    c=[[0]*31 for _ in range(n)]
    for i in range(k):
        l,r,x=ops[i]
        l-=1
        r-=1
        for j in range(31):
            if x&(1<<j):
                c[l][j]+=1
                if r+1<n:c[r+1][j]-=1
    for j in range(31):c[0][j]%=2
    for i in range(1, n):
        for j in range(31):
            c[i][j]+=c[i-1][j]
            c[i][j]%=2
    r=[0]*n
    for i in range(n):
        s=0
        for j in range(31):
            if c[i][j]:s+=(1<<j)
        r[i]=s
    return r
n=4
k=3
ops=[[1,3,2],[2,4,4],[1,4,6]]
print(find_array(n,k,ops))
