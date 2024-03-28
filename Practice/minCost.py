# def min_cost_ternary_array(N, A):
#     total_cost = 0
#     for i in range(N):
#         min_cost = float('inf')
#         for j in range(3):
#             cost = abs(A[i] - j)
#             if cost < min_cost:
#                 min_cost = cost
#         total_cost += min_cost
#     return total_cost

# N = int(input())
# A = list(map(int, input().split()))

# print(min_cost_ternary_array(N, A))
