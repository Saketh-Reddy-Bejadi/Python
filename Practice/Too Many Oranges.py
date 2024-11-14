for _ in range(int(input())):
    n,s=map(int,input().split())
    m1=10*n 
    m2=12*n 
    print('YES' if m1<=s <=m2 else 'NO')
    