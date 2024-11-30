import math
for _ in range(int(input())):
    a,z=map(int,input().split())
    print((a*z)//math.gcd(a,z))