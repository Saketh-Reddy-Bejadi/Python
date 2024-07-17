def valid(A,N):
    ele=None
    c=0
    for num in A:
        if c==0:
            ele = num
        c += (1 if num == ele else -1)
    
    if A.count(ele) > N / 2:
        return ele
    else:
        return -1

arr= [3,1,3,3,2]
n = 5
print(valid(arr,n))