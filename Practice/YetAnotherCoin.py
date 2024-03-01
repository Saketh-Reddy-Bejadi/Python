# def min_coins(n):
#     coins = [1, 3, 6, 10, 15]
#     dp = [float('inf')] * (n + 1)
#     dp[0] = 0
#     for coin in coins:
#         for j in range(coin, n + 1):
#             dp[j] = min(dp[j], dp[j - coin] + 1)
#     return dp[n]
# t =int(input())
# for i in range(0,t):
#     n=int(input())
#     print(min_coins(n))

def min_coins(n):
    coins = [1, 3, 6, 10, 15]
    min_coins = [0] * (n + 1)

    for i in range(1, n + 1):
        min_coins[i] = float('inf')
        for coin in coins:
            if i - coin >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(min_coins(n))
