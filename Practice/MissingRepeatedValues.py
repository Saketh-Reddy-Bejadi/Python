def valid(grid):
    visited=set()
    gridSum=Elecount=missingEle=0
    for i in range(len(grid)):
        gridSum+=sum(grid[i])
        Elecount+=len(grid[i])
        for j in range(len(grid[i])):
            if grid[i][j] in visited:
                missingEle=grid[i][j]
                break
            else:
                visited.add(grid[i][j])
    return [missingEle,int((Elecount*(Elecount+1))/2-gridSum+missingEle)]
    


print(valid([[1,3],[2,2]]))