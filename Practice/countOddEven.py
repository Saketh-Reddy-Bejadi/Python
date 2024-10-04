def valid(arr):
    evenCount=oddCount=0
    for n in arr:
        if n%2==0:evenCount+=1
        else:oddCount+=1
    return [oddCount,evenCount]

print(valid([1,2,3,4,5]))