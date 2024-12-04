def isEven(s,n):
    for i in range(len(s)-1,-1,-1):
        if s[i]!='.' and int(s[i])>0 and int(s[i])%2==0:
            return 1
        elif s[i]!='.' and int(s[i])>0 and int(s[i])%2!=0:
            return 0
        
print("EVEN" if isEven('4.100',5) else "ODD")