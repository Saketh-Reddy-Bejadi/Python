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
v=[]
q=[]
def bfs(v,graph,node):
    v.append(node)
    q.append(node)
    while q:
        m=q.pop(0)
        print(m,end=' ')
        for n in graph[m]:
            if n not in v:
                v.append(n)
                q.append(n)

bfs(v,graph,'A')
