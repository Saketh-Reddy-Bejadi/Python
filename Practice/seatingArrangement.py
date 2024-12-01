def valid(n,m,k):
    if((k*m)<n):
        return -1
    if m==1 or k>=n:
        return n
    n-=k
    z=(n+(m-2))/(m-1)
    return (k-int(z))

print(valid(4,20,7))