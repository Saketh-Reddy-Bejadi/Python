def valid(A):
    words = A.split()[::-1]
    r=''
    for i in words:
        r+=(" " +i)
    return r.strip()


A="the sky is blue"
print(valid(A))