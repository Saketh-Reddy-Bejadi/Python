import math

def binary(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            while x % i == 0:
                x //= i
            if x == 1:
                return True
            else:
                return False
    return x == 1

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        if binary(n):
            print("YES")
        else:
            print("NO")

solve()
