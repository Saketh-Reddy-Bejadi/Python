for _ in range(int(input())):
    x,y=map(int,input().split())
    maxV=max(x,y)
    minV=min(x,y)
    ans1=max(0,minV-(maxV//2))
    ans2=max(0,2*minV-maxV)
    print(min(ans1,ans2))