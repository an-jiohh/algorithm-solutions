from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]

def bfs(start) :
    queue = deque([start])
    visited = [0] * n
    while queue :
        now = queue.popleft()
        for i in range(n):
            if graph[now][i] == 1 and visited[i] == 0 :
                visited[i] = 1
                queue.append(i)
    return visited

for node in range(n):
    print(*bfs(node))