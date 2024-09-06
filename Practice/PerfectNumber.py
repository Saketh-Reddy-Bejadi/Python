import math
def valid(num):
    res=0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0 :
            res+=i
            if num/i!=1:
                res+=num//i
    return res==num*2
print(valid(6))