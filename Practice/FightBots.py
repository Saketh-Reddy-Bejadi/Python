for _ in range(int(input())):
    n,x2,y2=map(int,input().split())
    s=input()
    res='No'
    x1=y1=0
    for i in range(len(s)):
        if s[i]=='R':
            x1+=1 
        elif s[i]=='D':
            y1-=1 
        elif s[i]=='L':
            x1-=1 
        elif s[i]=='U':
            y1+=1 
        d=abs(x1-x2)+abs(y1-y2)
        if d<=i+1 and (i+1-d)%2==0:
            res="Yes"
            break
    print(res)
