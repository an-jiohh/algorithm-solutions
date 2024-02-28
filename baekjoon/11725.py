import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

edges = {}

for i in range(n-1) :
    start, end = map(int, input().split())
    edges[start] = edges.get(start, []) + [end]
    edges[end] = edges.get(end, []) + [start]

queue = deque([1])
visited = {1:1}

while queue :
    node = queue.popleft()
    for end in edges[node] :
        if end not in visited :
            visited[end] = node
            queue.append(end)

for i in range(2,n+1) :
    print(visited[i])