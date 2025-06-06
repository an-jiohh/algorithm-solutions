# 선수과목 이수후 해당과목을 이수
# 한학기에 들을 수 있는 과목수 제한 X
# 각 과목을 이수하려면 최소 몇학기가 걸리는지?
# 최대 이전 수강과목이 긴 과목을 찾는문제
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
increase = [0] * (n+1)
dp = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    increase[b] += 1

queue = deque()

for i in range(1,n+1):
    if increase[i] == 0 :
        dp[i] = 1
        queue.append(i)

while queue :
    node = queue.popleft()
    for i in graph[node] :
        increase[i] -= 1
        if increase[i] == 0:
            dp[i] = dp[node] + 1
            queue.append(i)
print(*dp[1:])