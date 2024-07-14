def valid(password):
    if len(password)<8:
        return False
    u=l=d=s=False
    for i,c in enumerate(password):
        if i<len(password)-1:
            if password[i]==password[i+1]:
                return False
        ch=ord(c)
        if ch>=65 and ch<=90:
            l=True
        elif ch>=97 and ch<=122:
            u=True
        elif c.isdigit():
            d=True
        elif c in "!@#$%^&*()-+":
            s=True
    if u and l and d and s:
        return True
    return False
password = "IloveLe3tcode!"
print(valid(password))