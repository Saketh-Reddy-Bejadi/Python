def minTime(k,positions):
    positions.sort()
    noOf=len(positions)
    ans=float('inf')
    for i in range(noOf-k+1):
        p=positions[i]
        q=positions[i+k-1]
        m=abs(p)+(q-p)
        n=abs(q)+(q-p)
        ans=min(ans,m,n)
    return ans
print(minTime(2,[2,-1,4]))
