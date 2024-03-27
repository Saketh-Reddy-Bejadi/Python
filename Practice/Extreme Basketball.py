n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    d=max(x,y)-min(x,y)
    if x-y>=10:
        print(0)
    else:
        y+=10
        y=y-x
        c=0
        while(y>3):
            y-=3
            c+=1
        if y!=0:
            c+=1
        print(c)
            