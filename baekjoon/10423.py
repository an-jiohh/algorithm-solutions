# 발전소는 이미 특정 도시에 건설되어 있고
# 이블을 설치할 때 드는 비용이 전부

import sys

input = sys.stdin.readline

n,m,k = map(int, input().split())
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_y != root_x :
        parent[root_y] = root_x
for i in list(map(int, input().split())) :
    union(0,i)

graph = []

for i in range(m):
    a,b,c = map(int, input().split())
    graph.append((c,a,b))
    graph.append((c,b,a))

graph.sort()
answer, count = 0, 0
for c,a,b in graph :
    if find(a) != find(b) :
        union(a,b)
        count += 1
        answer += c
        if count == n-1:
            break
print(answer)
