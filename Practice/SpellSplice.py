def valid(n):
        n.sort(key=lambda x:x[1],reverse=True)
        mSum=0
        l=min(100,n)
        for i in range(l):
            for j in range(i+1,l):
                cSum=n[i][1]*n[j][0]+n[i][0]*n[j][1]
                mSum=max(mSum,cSum)
        return mSum
for _ in range(int(input())):
    n=int(input())
    spells=[]
    for i in range(n):
        x,y=map(int,input().split())
        spells.append([x,y])
    print(valid(spells))