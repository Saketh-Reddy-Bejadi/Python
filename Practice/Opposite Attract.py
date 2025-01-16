t=int(input())
for i in range(t):
    l=int(input())
    r=''
    s=input()
    for c in s:
        if c=='0':r+='1'
        else:r+='0'
    print(r)