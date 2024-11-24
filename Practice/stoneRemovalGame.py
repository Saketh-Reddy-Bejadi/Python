def canAliceWin(n):
    p=10
    while(n>=p):
        n-=p
        q=p-1
        if n<q:
            return True
        n-=q
        p=q-1
    return False

print(canAliceWin(12))