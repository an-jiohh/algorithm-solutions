import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

nodes = [[] for i in range(n+1)]

for i in range(m) :
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [False for i in range(n+1)]

def dfs(node) :
    if visited[node] :
        return
    visited[node] = True
    for i in nodes[node] :
        dfs(i)

answer = 0
for j in range(1, n+1):
    if visited[j] == False :
        dfs(j)
        answer += 1
print(answer)