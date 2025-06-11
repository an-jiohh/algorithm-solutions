# 트리의 지름 = 임의의 두 점 사이의 거리 중 가장 긴것

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v = int(input())

graph = [[] for _ in range(v+1)]

for i in range(v):
    arr = list(map(int, input().split()))
    now = arr[0]
    for j in range(1, len(arr), 2):
        if arr[j] == -1 : break
        next, cost = arr[j], arr[j+1]
        graph[now].append((next, cost))

def dfs(node, cost):
    global visited
    for n, c in graph[node]:
        if not visited[n] :
            visited[n] = cost + c
            dfs(n, cost + c)

visited = [0] * (v+1)
visited[1] = 1
dfs(1,0)
next_start, max_num = 0, 0
for i in range(len(visited)) :
    if visited[i] > max_num :
        max_num = visited[i]
        next_start = i

visited = [0] * (v+1)
visited[next_start] = 1
dfs(next_start,0)
print(max(visited))