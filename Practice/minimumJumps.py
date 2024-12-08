import math
def valid(n):
        s=int(math.sqrt(n))
        return s*s==n
def minimumJump(points):
    x,i=0,0
    while(i<len(points)-1): 
        y=False
        if(valid(points[i])):
            for j in range(len(points)-1,i,-1):
                if(valid(points[j])):
                    x+=1
                    i=j-1
                    y=True
                    break
        if(not(y)):
            x+=1
        i+=1
    return x

points=[1,2,4]
print(minimumJump(points))