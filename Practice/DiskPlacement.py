import math
def valid(n):
    res=0
    # a=1
    # b=n-a
    # while a<=b:
    #     if a*b>res:
    #         res=a*b
    #     a+=1
    #     b-=1
    a=n//2
    b=math.ceil(n/2)
    return a*b

print(valid(7))
    