def baseNeg2(n):
    if n==0: return '0'
    s=''
    while(n!=0):
        r=n%2
        s=str(r)+s
        n=-(n//2)
    return s
    
print(baseNeg2(n = 2))