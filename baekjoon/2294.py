#점화식
#ns(n, k) = ds(n, k-coin[n]) + 1 / ds(n-1, k)
n, k = map(int, input().split())

coin = [int(input()) for i in range(n)]

dp = [[10**9]*(k+1) for i in range(n)]

for i in range(n):
    dp[i][0] = 0
    for j in range(1, k+1):
        if 0 <= j-coin[i] :
            dp[i][j] = min(dp[i-1][j], dp[i][j-coin[i]]+1)
        else :
            dp[i][j] = dp[i-1][j]

if dp[n-1][k] == 10**9 : dp[n-1][k] = -1
print(dp[n-1][k])