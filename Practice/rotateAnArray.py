def valid(arr,d):
    n=len(arr)
    d=d%n
    def reverse(arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    reverse(arr,0,n-1)
    reverse(arr,0,n-d-1)
    reverse(arr,n-d,n-1)
    return arr
    
print(valid([-1, -2, -3, 4, 5, 6, 7],2))