def func(arr):
    c=0
    for i in range(len(arr)):
        if arr[i]%2!=0:
            c+=1
            if c==3:
                return True
        else:
            c=0
    return False
arr = [1,2,34,3,4,5,7,23,12]
print(func(arr))