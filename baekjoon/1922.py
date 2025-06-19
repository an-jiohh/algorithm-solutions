# ## 크루스칼
# import sys

# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# graph = [list(map(int,input().split())) for i in range(m)]

# parent = [i for i in range(n+1)]

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
# def union(x,y):
#     root_x = find(x)
#     root_y = find(y)
#     if root_x != root_y :
#         parent[root_y] = root_x
# graph.sort(key=lambda x:x[2])
# answer, count = 0, 0
# for a,b,c in graph :
#     if find(a) != find(b):
#         union(a,b)
#         answer += c
#         count += 1
#     if count == n - 1 :
#         break
# print(answer)

## 프림
import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

edge = [list(map(int,input().split())) for i in range(m)]

graph = [[] for i in range(n+1)]
for a,b,c in edge :
    graph[a].append((c,b))
    graph[b].append((c,a))

visited = [False] * (n+1)
queue = [(0,1)]

answer = 0
while queue:
    cost, start = heapq.heappop(queue)
    if not visited[start] :
        visited[start] = True
        answer += cost
        for cost, end in graph[start] :
            if not visited[end] :
                heapq.heappush(queue, (cost, end))

print(answer)
