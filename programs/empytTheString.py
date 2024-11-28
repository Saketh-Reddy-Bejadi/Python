for _ in range(int(input())):
    n=int(input())
    s=input()
    a,b,t=0,0,0
    for c in s:
        if c=="A":
            if b>0:
                b-=1
                a+=1
            else:
                t+=1
                a+=1
        else:
            if a>0:
                a-=1
                b+=1
            else:
                t+=1
                b+=1
    print(t)