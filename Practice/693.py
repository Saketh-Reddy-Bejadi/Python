def sol(n):
    n=str(bin(n))
    n=n[2:]
    print(n)
    r=[]
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]!=n[j]:
                r.append(1)
            else:
                r.append(0)
            break
    if 0 in r:
        return False
    else:
        return True
n=11
print(sol(n))