def valid(matrix,target):
    if (len(matrix)==1):
        if target in matrix or target in matrix[0]:
            return True
        else:
            return False
    for i in range(len(matrix)):
        if target in matrix[i]:
            return True
    return False
    
print(valid([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))


