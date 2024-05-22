mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
n=1
while(mat!=target and n<=3):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i<=j:
                mat[i][j],mat[j][i]=mat[j][i], mat[i][j] 
        mat[i]=mat[i][::-1]
    n+=1
print(mat==target)