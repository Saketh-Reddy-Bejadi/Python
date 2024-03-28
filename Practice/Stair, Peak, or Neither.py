t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if x<y<z:
        print("STAIR")
    elif x<y>z:
        print("PEAK")
    else:
        print("NONE")
