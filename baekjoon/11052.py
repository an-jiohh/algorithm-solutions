n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(n+1)]

arr.insert(0,0)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j] + arr[j], dp[i])

print(dp[n])