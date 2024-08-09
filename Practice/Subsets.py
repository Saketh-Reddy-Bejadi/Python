def validate():
    arr=[10,5,-3]
    n=len(arr)
    k=2
    for i in range(0,(1<<n)):
        sum=0
        for j in range(0,n):
            if(i>>j)%2==1 :
                sum+=arr[j]
        if sum==k:
            return True
    return False
print(validate())