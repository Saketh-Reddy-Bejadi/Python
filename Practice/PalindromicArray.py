def valid(arr):
    for i in range(len(arr)):
        temp=int(str(arr[i])[::-1])
        if temp!=arr[i]:
            return False
    return True

print(valid( [121, 131, 20]))
            