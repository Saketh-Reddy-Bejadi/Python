def valid(arr):
    if len(arr)<2:
        return [-1]
    elif len(arr)==2:
        arr.sort()
        return [arr[0],arr[-1]]
    smallest=secondSmallest=float('inf')
    for n in arr:
        if n<smallest:
            secondSmallest=smallest
            smallest=n
        elif n<secondSmallest and n!=smallest:
            secondSmallest=n
    return [smallest, secondSmallest]


print(valid([2, 4, 3, 5, 6]))