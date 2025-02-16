def countSubarrays(arr, k):
    s,c=0,0
    d={}
    for n in arr:
        s+=n
        if(s==k):c+=1
        if(s-k in d):c+=d[s-k]
        d[s]=d.get(s,0)+1
    print(d)
    return c

print(countSubarrays([9,4,20,3,10,5],33))