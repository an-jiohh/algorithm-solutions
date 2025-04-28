from collections import deque

n, m = map(int, input().split())

nodes = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

answer = n
count = n * m

for i in range(n, 0, -1):
    queue = deque([(i, 0)]) 
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    temp = 0

    while queue:
        now, dist = queue.popleft()
        temp += dist

        for j in nodes[now]:
            if not visited[j]:
                visited[j] = True
                queue.append((j, dist + 1)) 

    if count >= temp:
        count = temp
        answer = i

print(answer)

"""
# 각 세대간 count를 착각
# 두번째 for문부터 문제 발생

from collections import deque

n, m = map(int, input().split())

nodes = [[] for i in range(n + 1)]

for i in range(m):
    a,b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

answer = n
count = n * m
for i in range(n, 0, -1):
    check = 0
    temp = 0
    queue = deque([i])
    visited = [True for i in range(n+1)]
    visited[i] = False
    while queue :
        now = queue.popleft()
        temp += check
        for j in nodes[now] :
            if visited[j] :
                visited[j] = False
                queue.append(j)
        check += 1
    if count >= temp :
        count = temp
        answer = i

print(answer)
"""