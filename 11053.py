n = int(input())

arr = list(map(int, input().split()))
dp = []
for i in range(n) :
    dp.append(1)
    for j in range(i) :
        if arr[i] > arr[j] and dp[i] <= dp[j] :
            dp[i] = dp[j] + 1
print(max(dp))