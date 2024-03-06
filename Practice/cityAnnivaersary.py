import math

def leastFlagstones(n, m, a):
    rows = math.ceil(n / a)
    cols = math.ceil(m / a)
    
    total_flagstones = rows * cols
    
    return total_flagstones

n, m, a = map(int, input().split())
print(leastFlagstones(n, m, a))