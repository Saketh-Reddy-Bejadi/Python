def solution(n,t):
    def check(n):
        a=1
        while n>0:
            a*=n%10
            n//=10
        return a
    while(True):
        if(check(n)%t==0):return n
        n+=1