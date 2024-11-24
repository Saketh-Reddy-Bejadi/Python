for _ in range(int(input())):
    s=input().strip()
    n=len(s)
    r='-1'
    f=False
    for i in range(n-1):
        if s[i]==s[i+1]:
            r=s[i:i+2]
            f=True
            break
    if not f:
        for i in range(n-2):
            x,y,z=s[i],s[i+1],s[i+2]
            if x!=y and x!=z and y!=z:
                r=s[i:i+3]
                f=True
                break
    print(r)