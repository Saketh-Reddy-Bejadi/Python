for _ in range(int(input())):
    z=input()
    l=len(z)
    c=0
    f=False
    for i in range(l):
        j=i+1
        if(j<l and z[i]==z[j]):
            f=True
            break
    if f:c+=1
    else:c+=len(z)

    print(c)