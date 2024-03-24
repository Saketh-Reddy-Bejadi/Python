def c(k):
    if k == 1:
        return 0
    arr=[1]
    count=0
    while(True):
        if sum(arr)>=k:
            break
        for i in range(len(arr)):
            arr[i]+=1
        count+=1
        if sum(arr)>=k:
            break
        arr.append(arr[0])
        count+=1
    return count

k=11
print(c(k))