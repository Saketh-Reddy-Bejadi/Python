# from itertools import permutations
# v = 4
# def travellingSalesmanProblem(graph, s):
#     vertex = []
#     for i in range(v):
#         if i != s:
#             vertex.append(i)
#     min_path = float('inf')
#     next_permutation = permutations(vertex)
#     for i in next_permutation:
#         current_pathweight = 0
#         k = s
#         for j in i:
#             current_pathweight += graph[k][j]
#             k = j
#         current_pathweight += graph[k][s]
#         min_path = min(min_path, current_pathweight)
#     return min_path
from itertools import permutations
v=4
def travellingSalesmanProblem(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    m=float("inf")
    per=permutations(vertex)
    for i in per:
        c=0
        k=s
        for j in i:
            c+=graph[k][j]
            k=j
        c+=graph[k][s]
        m=min(m,c)
    return m

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(travellingSalesmanProblem(graph, s))
