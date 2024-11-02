for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    l=0
    r='NO'
    while l<a-1:
        if((abs(b[l]-b[l+1])==5) or (abs(b[l+1]-b[l])==7)):
            r='YES'
            l+=1
        else:
            r='NO'
            break
    print(r)