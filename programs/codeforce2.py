import math
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    
    graph = defaultdict(list)
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    leaf_count = 0
    for i in range(1, n+1):
        if len(graph[i]) == 1:
            leaf_count += 1
            
    print(math.ceil(leaf_count/2))