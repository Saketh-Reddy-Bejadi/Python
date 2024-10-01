def valid(k,arr):
    arr[k-1],arr[len(arr)-k]=arr[len(arr)-k],arr[k-1]
    return arr

print(valid(3,[1, 2, 3, 4, 5, 6, 7, 8]))