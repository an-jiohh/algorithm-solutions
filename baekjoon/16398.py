# T에서 N개의 행성간의 플로우
# 플로우 관리비용을 최소로

# ## 크루스칼
# import sys

# n = int(input())

# arr = [list(map(int, input().split())) for i in range(n)]

# graph = []

# for i in range(n) :
#     for j in range(i+1,n) :
#         cost = arr[i][j]
#         graph.append((i,j,cost))

# parent = [i for i in range(n)]

# def find(x):
#     if parent[x] != x :
#         parent[x] = find(parent[x])
#     return parent[x]
# def union(x,y):
#     root_x = find(x)
#     root_y = find(y)
#     if root_x != root_y :
#         parent[root_x] = root_y

# graph.sort(key=lambda x:x[2])
# answer,count = 0, 0
# for a,b,c in graph :
#     if find(a) != find(b) :
#         union(a,b)
#         answer += c
#         count += 1
#     if count == n-1:
#         break
# print(answer)


## 프림
import sys
import heapq

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

graph = {}

for i in range(n) :
    temp = []
    for j in range(n) :
        if i != j :
            cost = arr[i][j]
            temp.append((cost,j))
    graph[i] = temp

visited = [False] * (n)
queue = [(0,0)]

answer = 0

while queue :
    cost, node = heapq.heappop(queue)
    if not visited[node]:
        visited[node] = True
        answer += cost
        for c, n in graph[node] :
            if not visited[n] :
                heapq.heappush(queue, (c,n))

print(answer)