import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

time = [0] 
edge = [[] for _ in range(n+1)]
increase = [0] * (n+1)

for i in range(1,n+1):
    arr = list(map(int, input().split()))
    arr.pop()
    time.append(arr[0])
    for j in range(1, len(arr)):
        node = arr[j]
        edge[node].append(i)
        increase[i] += 1

dp = [0] * (n+1)
queue = deque()

for i in range(1, n+1):
    if increase[i] == 0 :
        queue.append(i)
        dp[i] = time[i]

while queue :
    node = queue.popleft()
    for i in edge[node] :
        increase[i] -= 1
        dp[i] = max(dp[node] + time[i], dp[i])
        if increase[i] == 0 :
            queue.append(i)

for i in range(1, n+1):
    print(dp[i])