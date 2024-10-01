def valid(arr,x):
    smallerCount=largerCount=0
    for n in arr:
        if n <= x:
            smallerCount+=1
        if n >= x:
            largerCount+=1
    return [smallerCount,largerCount]

arr = [1, 5, 8, 12, 12, 12, 19]
x = 12
print(valid(arr, x))