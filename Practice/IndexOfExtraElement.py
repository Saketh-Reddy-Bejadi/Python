def valid(n,arr1,arr2):
    for i in range(n):
        if arr1[i] != arr2[i]:
            return i

n = 7
arr1= [2,4,6,8,9,10,12]
arr2 = [2,4,6,8,10,12]
print(valid(n, arr1, arr2))