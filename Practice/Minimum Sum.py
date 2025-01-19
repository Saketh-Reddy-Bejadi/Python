def valid(arr,change,k):
    t=sum(arr)
    d=[change[i]-arr[i] for i in range(len(arr))]
    d.sort()
    for i in range(k):
        t+=d[i]
    return t
arr = [0, 0, -3, 2, -7, 0, 1, 10]
change = [-5, -10, 3, -5, -4, 4, 6, 3]
k=1
print(valid(arr,change,k))