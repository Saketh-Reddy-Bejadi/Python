def valid(arr):
    n=len(arr)
    arr.sort()
    return arr[int(n/2)] if n%2==0 else arr[int(n/2-1)]

print(valid( [8, 1, 2, 9, 4, 3, 7, 5]))