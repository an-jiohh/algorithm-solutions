# 물이 흐르는 방향이 간선의 방향,
# 노드는 시작하는 곳 또는 합쳐지거나 만나는 곳, 바다와 만나는 곳
# strahler 
# 노드의 순서는 1
# 들어온는 강의 순서 중 큰 값을 i -> 1개이면 i, 2개 이상이면 i+1

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for test_number in range(1,t+1):
    k, m, p = map(int, input().split())

    graph = [[] for _ in range(m+1)]
    increase = [0] * (m+1)
    dp = [0] * (m+1)
    check = [0] * (m+1)

    for i in range(p):
        a, b = map(int ,input().split())
        graph[a].append(b)
        increase[b] += 1

    queue = deque()

    for i in range(1,m+1):
        if increase[i] == 0 :
            queue.append(i)
            dp[i] = 1
    
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if dp[next] < dp[node] :
                dp[next] = dp[node]
                check[next] = 0
            elif dp[next] == dp[node] :
                check[next] = 1
            increase[next] -= 1
            if increase[next] == 0:
                if check[next] == 1 :
                    dp[next] += 1
                queue.append(next)
    print(test_number, dp[m])