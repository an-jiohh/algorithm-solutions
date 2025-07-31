"""import sys

input = sys.stdin.readline

n = int(input())
graph = {i:[] for i in range(1,n+1)}
check = [0] * (n+1)

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)


def dfs(node, check, count):
    if not graph[node]:
        return not check
    for i in graph[node]:
        temp = 10**9
        if check : temp = min(temp, dfs(i, 0, count))
        temp = min(temp, dfs(i, 1, count+1))
    return temp
print(dfs(1,1,0))"""

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
graph = {i:[] for i in range(1,n+1)}
dp = [[0,0] for i in range(n+1)] # dp[node][0]: 얼리, dp[node][1]: 일반
visited = [False] * (n+1)

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b) #어떤 순서로 들어올지 모름
    graph[b].append(a)



def dfs(node):
    dp[node][0] = 1
    for i in graph[node]:
        if not visited[i] :
            visited[i] = True
            dfs(i) 
            dp[node][0] += min(dp[i][0],dp[i][1])
            dp[node][1] += dp[i][0]

visited[1] = True
dfs(1) # 트리 이기 떄문에 어떤값으로 실행해도 그값이 루트가 되어 한뱡향으로 탐색, visited로 역뱡향 탐지 방지
print(min(dp[1][0],dp[1][1]))

