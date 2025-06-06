# 수행할 작업 n개, 걸리는 시간 존재
# 선행관계가 되어야할 작업들이있고, k번 작업에 대해 먼저해야하는 작업의 경우 1~k-1사이
# 선행관계에 있는 작업이 하나도 없는 작업도 하나이상 존재
# 작업 동시 수행가능, 최소 시간을 구하는 문제

import sys
from collections import deque

n = int(input())

graph = [[] for i in range(n+1)]
increase = [0] * (n+1)
time = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1,n+1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    increase[i] = arr[1]
    for j in range(arr[1]):
        node = arr[2+j]
        graph[node].append(i)

queue = deque()
for i in range(1, n+1):
    if increase[i] == 0 :
        queue.append(i)
        dp[i] = time[i]

while queue :
    node = queue.popleft()
    for i in graph[node]:
        dp[i] = max(dp[node]+time[i], dp[i])
        increase[i] -= 1
        if increase[i] == 0 :
            queue.append(i)
print(max(dp))