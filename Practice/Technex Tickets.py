for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    elif n%2==0:
        print(n//2+1)
    else:
        print((n-1)//2)