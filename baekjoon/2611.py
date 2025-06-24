# 자동차 경주를 진행하는데 1에서 1까지 돌아오는 많은 점수를 얻어 돌아오는 경우 우승
# 최대값을 구하는 문제인데, 갈 수 있는 모든 경우
# 결론 싸이클을 이용해야한다면, 위상정렬에서 사이클을 사용하지 않는 것이 좋음, 사이클 부분을 위상정렬에서 분리


"""
from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
increase = [0] * (n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    increase[b] += 1

dp = [0] * (n+1)
dp_root = [0] * (n+1)

queue = deque([1])

answer, answer_list = 0, [1]

while queue :
    node = queue.popleft()
    for nxt, cost in graph[node]:
        increase[nxt] -= 1
        if cost+dp[node] > dp[nxt] :
            dp[nxt] = cost+dp[node]
            dp_root[nxt] = node
        if increase[nxt] == 0 :
            queue.append(nxt)
print(dp[1])

if dp[1] == 0:
    print(1)
else :
    temp = dp_root[1]
    while temp != 1 and temp != 0:
        answer_list.append(temp)
        temp = dp_root[temp]
    answer_list.append(1)
    answer_list.reverse()
    print(*answer_list)
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph     = [[] for _ in range(n + 1)]
indegree  = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    if b != 1:              # 1번으로 향하는 간선은 제외
        indegree[b] += 1

dp      = [-10**9] * (n + 1)
parent  = [0] * (n + 1)
dp[1]   = 0

q = deque([1])
while q:
    u = q.popleft()
    for v, w in graph[u]:
        if dp[u] + w > dp[v]:
            dp[v] = dp[u] + w
            parent[v] = u
        if v != 1:          # indegree 관리도 v≠1
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

# 1로 돌아오는 간선 통해 점수 계산
best, last = 0, 0
for u in range(1, n + 1):
    for v, w in graph[u]:
        if v == 1 and dp[u] + w > best:
            best, last = dp[u] + w, u

print(best)

# 경로 역추적
path = [1]
cur = last
while cur != 1:
    path.append(cur)
    cur = parent[cur]
path.append(1)
print(*reversed(path))