def findSubarray(arr):
    d={}
    s,c=0,0
    for n in arr:
        s+=n
        if(s==0):c+=1
        if(s in d):
            c+=d[s]
        d[s]=d.get(s,0)+1
    return c

print(findSubarray([6, -1, -3, 4, -2, 2, 4, 6, -12, -7]))