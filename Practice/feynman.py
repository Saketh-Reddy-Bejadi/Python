while(True):
    n=int(input())
    if n==0:
        break
    sq=0
    for i in range(1,n+1):
        sq+=i*i
    print(sq)