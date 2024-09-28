def valid(maximumHeight):
    maximumHeight.sort()
    currentHeight,totalHeight = maximumHeight[-1],0
    for i in range(len(maximumHeight)-1, -1, -1):
        currentHeight=min(currentHeight,maximumHeight[i])
        if currentHeight <=0:
            return -1
        totalHeight += currentHeight
        currentHeight -=1
    return totalHeight
    
    
print(valid([2,2,1]))