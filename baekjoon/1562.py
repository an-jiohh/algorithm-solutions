MOD = 1_000_000_000
BIT = 1 << 10

n = int(input())

dp = [[[0] * BIT for _ in range(10)] for _ in range(n)]

for i in range(1,10):
    dp[0][i][1 << i] = 1

for i in range(1,n):
    for j in range(10):
        for k in range(BIT): #j가 가지고 있는 지금까지의 모든 경우의 수 = key, 횟수 = value
            next_bit = k | 1 << j
            if 0 < j :
                dp[i][j][next_bit] += dp[i-1][j-1][k]
            if j < 9 :
                dp[i][j][next_bit] += dp[i-1][j+1][k]
            
            dp[i][j][next_bit] %= MOD
answer = 0
for i in range(10):
    answer += dp[n-1][i][BIT-1]
    answer %= MOD
print(answer)