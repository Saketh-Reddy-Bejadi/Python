def valid(arr):
    return True if arr==arr[::-1] else False
    
print(valid([1, 2, 3, 2, 2]))