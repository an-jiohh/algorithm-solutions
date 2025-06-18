# N개의 집, M개의 길, 
# 두 개의 분리된 마을로 분할할 계획
# 각 분리된 마을 안에 집들이 서로 연결되도록 분할
# 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있음
# 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있음
# 풀이
# 최소 스패닝 트리로 만든 후 가장 큰 유지비를 사용하는 길을 없애면 자동으로 두개의 마을로 형성됨


import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

# 2904ms
# rank = [1] * (n+1)
# def union(x, y):
#     root_x = find(x)
#     root_y = find(y)
#     if root_x == root_y :
#         return
#     if rank[root_x] < rank[root_y] :
#         parent[root_x] = root_y
#     else :
#         parent[root_y] = root_x
#         if rank[root_x] == rank[root_y]:
#             rank[root_x] += 1

# 2812ms
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x < root_y :
        parent[root_y] = root_x
    else :
        parent[root_x] = root_y


graph = [list(map(int, input().split())) for i in range(m)]
graph.sort(key=lambda x:x[2])

answer,count, max_edge = 0,0,0
for a,b,c in graph :
    if find(a) != find(b) :
        union(a, b)
        answer += c
        count += 1
        max_edge = max(c, max_edge)
        if count == n - 1 :
            break
print(answer-max_edge)