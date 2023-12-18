MOD = 998244353

def solve(arr):
    n = len(arr)
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(i+1):
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            if j < i: 
                dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD
            
    ans = sum(dp[n]) % MOD
    return ans
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(solve(arr))