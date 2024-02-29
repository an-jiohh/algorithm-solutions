import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for i in range(n+1)]
node = [0] * (n+1)

for i in range(m) :
    start, end = map(int, input().split())
    edges[end].append(start)

for i in range(1,n+1) :
    queue = deque([i])
    visited = [False] * (n+1)
    visited[i] = True
    count = 1
    while queue :
        start = queue.popleft()
        for end in edges[start] :
            if not visited[end] :
                count += 1
                visited[end] = True
                queue.append(end)
    node[i] = count

answer_count = max(node)
for i in range(n+1) :
    if node[i] == answer_count :
        print(i, end=" ")