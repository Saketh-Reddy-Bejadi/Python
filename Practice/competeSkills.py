def valid(arr1,arr2):
    A=B=0
    for i in range(len(arr1)):
        if arr1[i]>arr2[i]:
            A+=1
        elif arr1[i]<arr2[i]:
            B+=1
    return [A,B]

print(valid([4,2,7],[5,2,8]))