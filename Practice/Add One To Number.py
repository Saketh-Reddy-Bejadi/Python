def valid(A):
    s=''.join(map(str,A))
    return list(str(int(s)+1))

print(valid([1,2]))