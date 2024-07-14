def valid(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:c+=1
    if c==3:return True
    return False
n=2
print(valid(n))