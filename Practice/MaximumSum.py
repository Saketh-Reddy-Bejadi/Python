def valid(n,arr,x):
    maxSet = float('-inf')
    maxUnset = float('-inf')
    temp = 1 << (x - 1)  

    for num in arr:
        if (num & temp) != 0: 
            maxSet = max(maxSet, num)
        else:  
            maxUnset = max(maxUnset, num)

    if maxSet == float('-inf') or maxUnset == float('-inf'):
        return -1

    return maxSet + maxUnset
n=5
arr=[1,5,9,23,12]
x=3
print(valid(n,arr,x))