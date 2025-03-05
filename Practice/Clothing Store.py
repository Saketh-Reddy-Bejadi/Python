for _ in range(int(input())):
    x,y,z,a,b,c=map(int,input().split())
    h=0
    h=min(z,c)
    z-=h 
    c-=h 
    yb=min(y,b)
    h+=yb
    y-=yb
    b-=yb
    if b>0:
        t=min(z,b)
        h+=t 
        z-=t  
        b-=t
    xa=min(x,a)
    h+=xa
    x-=xa 
    a-=xa
    a-=min(x,a)
    if a>0:
        t=min(y,a)
        h+=t 
        y-=t  
        a-=t
    if a>0:
        t=min(z,a)
        h+=t 
        z-=t  
        a-=t
    print(h)