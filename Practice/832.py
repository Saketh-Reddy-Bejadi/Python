def flipAndInvertImage(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j]==0:
                image[i][j]=1
            else:
                image[i][j]=0
        image[i].reverse()
    return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))