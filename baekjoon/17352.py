# n개의 섬, n-1다리가 있어 통행이 가능했으나
# 다리하나를 없앴을때, 서로 왕복할 수 없는 섬들이 생겼다.
# 이때 다리하나를 건설해서 연결해라

import sys

input = sys.stdin.readline

n = int(input())

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
        if rank[root_x] == rank[root_y]:
            rank[root_x] +=1

for i in range(n-2):
    a, b = map(int, input().split())
    union(a,b)

answer = set()
for i in range(1, n+1):
    answer.add(find(i))
answer = list(answer)
print(answer[0], answer[1])