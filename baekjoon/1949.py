# '우수 마을'로 선정된 마을 주민 수의 총 합을 최대로 해야 한다.
# 두 마을이 인접해 있으면 두 마을을 모두 '우수 마을'로 선정할 수 없음
# '우수 마을'로 선정되지 못한 마을은 적어도 하나의 '우수 마을'과는 인접해 있어야함
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
city = list(map(int, input().split()))

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0,0] for i in range(n+1)]
visited = [False] * (n+1)

def dfs(node):
    dp[node][1] = city[node-1]
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            dfs(child)
            dp[node][1] += dp[child][0] 
            dp[node][0] += max(dp[child][0], dp[child][1])
visited[1] = True
dfs(1)
print(max(dp[1][0], dp[1][1]))
