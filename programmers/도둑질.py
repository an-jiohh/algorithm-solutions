def solution(money):
    answer = 0
    n = len(money)
    O_dp = [0] * n
    X_dp = [0] * n
    
    X_dp[1] = money[1]
    for i in range(2, n):
        X_dp[i] = max(money[i]+X_dp[i-2],X_dp[i-1])
    O_dp[0] = money[0]
    O_dp[1] = max(money[0], money[1])
    for i in range(2, n-1):
        O_dp[i] = max(money[i]+O_dp[i-2],O_dp[i-1])
    answer = max(X_dp[n-1], O_dp[n-2])
    return answer