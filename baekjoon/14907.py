import sys
from collections import deque

nodes = {}
increase = {}
graph = {}

for line in sys.stdin:
    index = line.strip().split()
    if len(index) == 3 : node, day, pre = index
    else : 
        node, day = index
        pre = []
    nodes[node] = int(day)
    for temp in list(pre):
        edges = graph.get(temp, [])
        edges.append(node)
        graph[temp] = edges
    increase[node] = increase.get(node, 0) + len(pre)

queue = deque()
dp = {}
for i in nodes :
    dp[i] = 0
    if increase[i] == 0 :
        queue.append(i)
        dp[i] = nodes[i]
    

while queue :
    node = queue.popleft()
    for i in graph.get(node,[]):
        increase[i] -= 1
        dp[i] = max(dp[i], dp[node]+nodes[i])
        if increase[i] == 0 :
            queue.append(i)
print(max(dp.values()))