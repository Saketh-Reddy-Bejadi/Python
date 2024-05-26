for _ in range(int(input())):
    moves,cubes=map(int,input().split())
    if moves>=cubes and (moves-cubes)%2==0:
        print("Yes")
    else:
        print("No")