import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
increase = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    increase[b] += 1

answer = []
queue = deque()
for i in range(1, n+1):
    if increase[i] == 0:
        queue.append(i)

while queue :
    node = queue.popleft()
    answer.append(node)
    for i in graph[node]:
        increase[i] -= 1
        if increase[i] == 0 :
            queue.append(i)

print(*answer)