# 모든 도로 일방통행, 싸이클없음
# 많은 사람들이 시작도시에서 도착도시까지 
# 모든사람들이 도착도시에서 만남
# 어떤 사람은 이 시간에 만나기 위하여 1분도 쉬지 않고 달려야 한다. 이런 사람들이 지나는 도로의 수를 카운트 
# 가장 오래걸리는 사람은 계속달려야함, 가장 오래걸리는 시간일때 거쳐간 도시의 수와, 시간을 구는 문제
# 거쳐가는 도시의 개수와 시간은 반비례할 수 있음!
# 모든 경우의 수를 체크하기에는 시간복잡도가 너무큰듯
# 위상정렬로 도시까지 가장 오래걸리는 길을 선택하여 가장 오래걸리는 사람을 확인 -> 위상정렬

"""
# 역추적 X
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
increase = [0] * (n+1)
dp_time = [0] * (n+1)
dp_city = [0] * (n+1)


for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    increase[b] += 1

start, end = map(int, input().split())

queue = deque([start])

while queue:
    node = queue.popleft()
    for i in graph[node]:
        next, time = i
        if dp_time[next] < dp_time[node] + time :
            dp_time[next] = dp_time[node] + time
            dp_city[next] = dp_city[node] + 1
        elif dp_time[next] == dp_time[node] + time :
            dp_city[next] += dp_city[node] + 1
        increase[next] -= 1
        if increase[next] == 0 :
            queue.append(next)
print(dp_time[end])
print(dp_city)
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
increase = [0] * (n+1)
dp = [0] * (n+1)

for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    reverse_graph[b].append((a,t))
    increase[b] += 1

start, end = map(int, input().split())

queue = deque([start])

while queue:
    node = queue.popleft()
    for i in graph[node]:
        next, time = i
        dp[next] = max(dp[node]+time, dp[next]) 
        increase[next] -= 1
        if increase[next] == 0 :
            queue.append(next)

# bfs로 역추적
visited = [True] * (n+1)
queue = deque([end])
count = 0
while queue:
    node = queue.popleft()
    for i in reverse_graph[node]:
        prev, time = i
        if dp[node] - time == dp[prev] : #간선체크는 계속하되, 
            count += 1
            if visited[prev] : #노드방문은 한번만(간선체크 밑에있어 전체를 순회하진않음)
                visited[prev] = False
                queue.append(prev)
print(dp[end])
print(count)