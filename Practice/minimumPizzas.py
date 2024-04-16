for i in range(int(input())):
    x,y=map(int,input().split())
    while(x>=y):
        x*=4
    print(x)