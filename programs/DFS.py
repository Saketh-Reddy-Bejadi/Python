#depth first search(DFS)
graph1 = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

graph2 = {
    0: [1, 2],
    1: [2],
    2: [3, 4],
    3: [1, 2],
    4: []
}

visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph1, 'A')
print()
dfs(visited, graph2, 0)