def valid(arr1,arr2):
    start=[]
    for i in range(len(arr2)):
        start.append([arr2[i]]*arr1.count(arr2[i]))
        arr1=[x for x in arr1 if x != arr2[i]]
    start+=[arr1]
    res=[n for sub in start for n in sub]
    return res
    
# 2,2,2,1,4,3,3,9,6,7,19
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(valid(arr1, arr2))