def valid(heights):
    c=0
    temp=heights.copy()
    temp.sort()
    for i in range(len(heights)):
        if heights[i]!=temp[i]:
            c+=1
    return c

heights = [5,1,2,3,4]
print(valid(heights))