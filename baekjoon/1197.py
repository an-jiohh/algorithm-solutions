# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 문제
# V 정점, E 간선
# A, B, C 가중치

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e = map(int, input().split())

parent = [i for i in range(v+1)]
rank = [1] * (v+1)

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

# def union(x, y):
#     root_x = find(x)
#     root_y = find(y)
#     if root_x == root_y :
#         return
#     if rank[root_x] < rank[root_y] :
#         parent[root_x] = root_y
#     else:
#         parent[root_y] = root_x
#         if rank[root_x] == rank[root_y] :
#             rank[root_x] += 1

# rank가 없어도 시간복잡도가 차이나지 않음 232ms로 동일
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x < root_y :
        parent[root_y] = root_x
    else :
        parent[root_x] = root_y
graph = [list(map(int, input().split()))for i in range(e)]
graph.sort(key=lambda x:x[2])
count, answer = 0, 0
for a, b, cost in graph :
    if find(a) != find(b) :
        union(a,b)
        count += 1
        answer += cost
        if count == v-1:
            break
print(answer)