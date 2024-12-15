def minRemoval(arr):
    c=0
    for i in arr:
        if i<0:
            c+=1
    return c-1 if c==len(arr) else c

print(minRemoval([1,2,-5,3]))