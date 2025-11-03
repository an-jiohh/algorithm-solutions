## 점화식
## 0~9이므로 이전수에서 그수를 계속해서 더하면 풀이가능

n = int(input())

dp = [1] * 10

for i in range(1, n):
    for j in range(9,-1,-1):
        for k in range(j-1,-1,-1):
            dp[j] += dp[k]
print(sum(dp)%10007)