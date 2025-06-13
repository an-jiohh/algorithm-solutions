# 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있음
# 두 개의 섬에 공장을 세워 두고 물품을 생산,  공장에서 다른 공장으로 생산 중이던 물품을 수송
# 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너짐
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값
# 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며
# 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어짐

import sys

input = sys.stdin.readline

n,m = map(int, input().split())

parent = [i for i in range(n+1)]
rank = [1] * (n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y :
        return
    if rank[root_x] < rank[root_y] :
        parent[root_x] = root_y
    else :
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y] :
            rank[root_x] += 1

rand = [list(map(int,input().split()))for i in range(m)]
rand.sort(key=lambda x:-x[2])

start, end = map(int, input().split())

for a,b,c in rand :
    union(a,b)
    if find(start) == find(end) == find(a) :
        print(c)
        break
