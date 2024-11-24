graph={
    'A': ['B', 'C','D'],
    'B': ['A','E','F'],
    'C': ['A','G','H'],
    'D': ['A','B'],
    'E': ['B'],
    'F': ['B'],
    'G': ['C'],
    'H': ['C','D']
}
v=set()
def dfs(node,v,graph):
    if node not in v:
        print(node)
        v.add(node)
        for i in graph[node]:
            dfs(i,v,graph)
dfs('A',v,graph)