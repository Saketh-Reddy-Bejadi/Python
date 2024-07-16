def valid(arr,n):
    visited=set()
    res=[]
    for i in range(len(arr)):
        if arr[i] in visited:
            res.append(arr[i])
        else:
            visited.add(arr[i])
            
    return res

n = 4
arr= [1, 2, 1, 3, 4, 3]
print(valid(arr,n))