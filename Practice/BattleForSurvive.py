for _ in range(int(input())):
    n=int(input())
    bat=list(map(int,input().split()))
    temp=bat[n-2]
    for i in range(n-3,-1,-1):
        temp-=bat[i]
    print(bat[n-1]-temp)