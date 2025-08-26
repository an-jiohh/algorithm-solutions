from heapq import heappop, heappush
import sys

input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())

graph = [[] for i in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

dist = [10**9] * (v+1)

queue = [(0, k)]
dist[k] = 0
while queue:
    c, check_node = heappop(queue)
    if dist[check_node] < c :
        continue
    for next_node, next_c  in graph[check_node]:
        if dist[next_node] > c + next_c :
            dist[next_node] = c + next_c
            heappush(queue, (c + next_c, next_node))
for i in dist[1:] :
    if i == 10**9 : 
        print("INF")
    else :
        print(i)