def valid(arr,k,sum):
    c=0
    freq={}
    for n in arr:
        if k-n in freq:
            c+=freq[k-n]
        if n in freq:
            freq[n]+=1
        else:
            freq[n]=1
    return c
k = 6
arr = [1, 5, 7, 1]
print(valid(arr,k,0))