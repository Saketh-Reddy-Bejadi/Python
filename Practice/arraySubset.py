def valid(a1,a2,n,m):
    a1Count = {}    
    for i in a1:
        if i in a1Count:
            a1Count[i] += 1
        else:
            a1Count[i] = 1    
    for i in a2:
        if i not in a1Count or a1Count[i] == 0:
            return 'No'
        else:
            a1Count[i] -= 1
    return 'Yes'

n,m=8,4
a1=[1,2,3,4,5,6,7,8]
a2=[1,2,3,1]
print(valid(a1,a2,n,m))

