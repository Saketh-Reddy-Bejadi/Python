def valid(arr):
    # arr.sort()
    # arr=arr[ind:]+arr[:ind][::-1]
    # i=0
    # j=len(arr)-1
    # while i<j:
    #     if arr[i]<0:
    #         arr[i],arr[j]=arr[j],arr[i]
    #         j-=1
    #     else:
    #         i+=1
    ind=0
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1 
    return arr
print(valid([1, -1, 3, 2, -7, -5, 11, 6 ]))