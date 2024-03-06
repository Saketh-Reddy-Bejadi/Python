t=int(input())
for _ in range(t):
    num = int(input())
    binum =bin(num)
    binum=(binum[2:])
    s=0
    for n in binum:
        s+=int(n)
    if s%2==0:
        print("EVEN")  
    else:
        print("ODD")
