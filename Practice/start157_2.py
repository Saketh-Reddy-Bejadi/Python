# Non-matching Name

for _ in range(int(input())):
    SAlen,SBlen=map(int,input().split())
    SAstr=input()
    SBstr=input()
    SAstr+=SBstr
    ans='No'
    Alphabets='abcdefghijklmnopqrstuvwxyz'
    for c in Alphabets:
        if c not in SAstr:
            ans='Yes'
    print(ans)