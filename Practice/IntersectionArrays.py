def valid(a,b,n,m):
    a=set(a)
    b=set(b)
    c=0
    for n in b:
        if n in a:
            c+=1
    return c
n = 5
m = 3
a = [89, 24, 75, 11, 23]
b = [89, 2, 4]
print(valid(a,b,n,m))