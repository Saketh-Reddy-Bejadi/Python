def maximumWealth(self, accounts: list[list[int]]) -> int:
    s1=m=0
    for c in accounts:
        for n in c:
            s1+=n
        m=max(m,s1)
    return m
m=[[1,2,3],[3,2,1]]
print(maximumWealth(None,m))