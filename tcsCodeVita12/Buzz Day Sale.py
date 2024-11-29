n=int(input())
a=list(map(int,input() .split()))
c=list(map(int,input() .split()))
b=int(input())
mf,mc=0,0
for i in range(n):
    bc=c[i]
    q=b//bc
    if q>0:
        f,c=0,0
        for j in range(n):
            if i!=j and a[i]%a[j]==0:
                f+=q
                c+=c[j]*q
        if f>mf or (f==mf and c>mc):
            mf,mc=f,c
print(f"{mf} {mc}",end="")