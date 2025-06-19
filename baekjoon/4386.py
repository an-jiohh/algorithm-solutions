#n개의 별들을 이어서 별자리를 만들때
#서로 다른 두 별을 일직선으로 이은 형태
#모든별은 선을 통해 서로 직/간접적으로 연결
#별자리를 만드는 최소 비용

# ## 프림
# import sys
# from collections import deque
# import heapq
# import math

# input = sys.stdin.readline

# n = int(input())

# arr = [tuple(map(float, input().split())) for i in range(n)]
# visited = [False] * (n)

# queue = [(0, n-1)]

# answer = 0
# while queue:
#     cost, start = heapq.heappop(queue)
#     if not visited[start] :
#         start_x, start_y = arr[start] 
#         visited[start] = True
#         answer += cost
#         for end in range(n) :
#             if not visited[end] :
#                 end_x, end_y = arr[end]
#                 cost = math.sqrt((end_x-start_x) ** 2 + (end_y-start_y) ** 2)
#                 heapq.heappush(queue, (cost, end))
# print(f"{answer:.2f}")

import sys
import math

input = sys.stdin.readline

n = int(input())

arr = [tuple(map(float, input().split())) for i in range(n)]

graph = set()

for start in range(n):
    start_x, start_y = arr[start]
    for end in range(n):
        if start != end : 
            end_x, end_y = arr[end]
            cost = math.sqrt((end_x-start_x) ** 2 + (end_y-start_y) ** 2)
            if start < end : graph.add((start, end, cost))
            else : graph.add((end, start, cost))

graph = list(graph)
graph.sort(key=lambda x:x[2])
gn = len(graph)

parent = [i for i in range(gn+1)]


def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x < root_y :
        parent[root_y] = root_x
    else :
        parent[root_x] = root_y

answer, count = 0, 0
for a, b, cost in graph:
    if find(a) != find(b) :
        union(a, b)
        answer += cost
        count += 1
    if count == n-1:
        break

print(f"{answer:.2f}")