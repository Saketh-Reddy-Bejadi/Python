for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    j=i+2
    t=[]
    for i in range(n-2):
        t.append(a[i:j+1])
        j+=1
    c=0
    # for i in range(len(t)):