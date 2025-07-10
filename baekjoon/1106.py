# 점화식
# n = 선택가능한 도시의 수, c = 남은 인원의 수
# ds(n, c) = min(ds(n,c), ds(n,c-N[n])+cost[n])

import sys

input = sys.stdin.readline

MAX = 10**9

c, n = map(int, input().split())

cost = []
customer = []

for i in range(n):
    a,b = map(int, input().split())
    cost.append(a)
    customer.append(b)

dp = [MAX] * (c+101)
dp[0] = 0

for i in range(n):
    for j in range(c+101):
        if j-customer[i] >= 0 :
            dp[j] = min(dp[j], dp[j-customer[i]] + cost[i])
        else :
            dp[j] = dp[j]
print(min(dp[c:]))