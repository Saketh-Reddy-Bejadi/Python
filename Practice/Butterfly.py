for _ in range(int(input())):
    r,g,b=map(int,input().split())
    if (r+g>=b and g+b>=r and r+b>=g):
        print("YES")
    else:
        print('NO')