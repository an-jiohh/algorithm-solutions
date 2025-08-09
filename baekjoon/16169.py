import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

c = [0] * (n+1)
c_num = [0] * (n+1)
t = [0] * (n+1)
graph = [[] for i in range(n+1)]
parent = [0] * (n+1)
increase = [0] * (n+1)

for i in range(1,n+1):
    a,b = map(int, input().split())
    c[i] = a
    t[i] = b
    c_num[a] += 1

for i in range(1,n+1):
    for j in range(1, n+1):
        if c[j] == c[i] + 1 : 
            graph[i].append(j)
            increase[j] += 1

dp = [0] * (n+1)
queue = deque()
for i in range(1, n+1):
    if increase[i] == 0 :
        queue.append(i)
        dp[i] = t[i]

while queue :
    node = queue.popleft()
    for i in graph[node]:
        increase[i] -= 1
        dp[i] = max(dp[i], dp[node] + t[i] + (node - i) ** 2)
        if increase[i] == 0 :
            queue.append(i)
print(max(dp))