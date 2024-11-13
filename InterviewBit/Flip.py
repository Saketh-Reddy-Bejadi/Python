def flip(A):
    g=[1 if ch=='0' else -1 for ch in A]
    m=c=s=0
    L=R=-1
    for i in range(len(g)):
        c+=g[i]
        if c>m:
            m=c
            L,R=s,i   
        if c<0:
            c=0
            s=i+1
    if m>0:return [L+1,R+1]
    else:return []
    
A="010"
print(flip(A))