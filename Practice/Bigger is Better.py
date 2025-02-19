for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=-1
    for c in range(ord('a'),ord('z')+1):
        t=chr(c)*n 
        if t>s and t[::-1]>s :
            ans=t
            break
    print(ans)