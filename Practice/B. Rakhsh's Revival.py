for _ in range(int(input())):
    n,m,k=map(int,input().split())
    s=input()
    a,c,i=0,0,0
    while(i<len(s)):
        if s[i]!='0':
            c=0
        else:
            c+=1
        if c==m:
            a+=1
            c=0
            i+=k-1
        i+=1
    print(a)