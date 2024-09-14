def valid(height,threshold):
    res=set()
    for i in range(1,len(height)):
        if height[i-1]==threshold:
            res.add(i)
    return list(res)
height = [10,1,10,1,10]
threshold = 3
print(valid(height,threshold))