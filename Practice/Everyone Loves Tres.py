for _ in range(int(input())):
    n=int(input())
    if n==1 or n==3:
        print(-1)
    elif n%2==0:
        print('33'*((n//2)-1)+'66')
    else:
        print('3'*(n-5)+'36366')