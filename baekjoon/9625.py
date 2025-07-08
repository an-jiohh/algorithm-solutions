"""
k = int(input())
a, b = 0,0
def dfs(strk, n):
    global a, b
    if n == k :
        if strk == "A" : a += 1
        else : b += 1
        return
    if strk == "B":
        dfs("A", n+1)
        dfs("B", n+1)
    else :
        dfs("B", n+1)
dfs("A", 0)
print(a,b)
"""

k = int(input())

dp = [0] * (k+1)
dp[1] = 1

for i in range(2,k+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[k-1], dp[k])
