def small(s,n):
    stringRev=s[::-1]
    if n%2==0:
        return s
    elif n%2!=0 :
        for i in range(min(len(s), len(stringRev))):
            if s[i] < stringRev[i]:
                flag= -1  
            elif s[i] > stringRev[i]:
                flag=1   
        if len(s) < len(stringRev):
            flag=-1 
        elif len(s) > len(stringRev):
            flag=1 
        if flag==-1:
            return stringRev
    else:
        s=(stringRev+s[:n-1])[::-1]*n-1
        return s
    
    

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(small(s,n))