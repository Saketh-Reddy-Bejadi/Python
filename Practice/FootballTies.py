import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    t=min(x,y)
    print(t%3)