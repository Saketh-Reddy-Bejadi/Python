def valid(flowerbed, n):
    if n==0:
        return True
    for i in range(0,len(flowerbed)):
        if flowerbed[i]!=0:
            continue
        left = False
        right = False
        if i-1<0:
            left=True
        elif flowerbed[i-1]==0:
            left=True
        if i+1>=len(flowerbed):
            right=True
        elif flowerbed[i+1]==0:
            right=True
        if left and right:
            flowerbed[i]=1 
            n-=1
            if n==0:
                return True

    return n==0


flowerbed = [0,0,1,0,0]
n = 1

print(valid(flowerbed,n))