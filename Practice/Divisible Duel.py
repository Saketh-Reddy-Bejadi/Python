for _ in range(int(input())):
    x,y=map(int,input().split())
    es,os=0,0
    for i in range(x,y+1):
        if(i%x==0):
            if(i%2==0):es+=1
            else:os+=1
    print("YES" if es>=os else "NO")