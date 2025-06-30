import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
node = [(0,0)]
graph = []

for i in range(n):
    x,y = map(int, input().split())
    node.append((x,y))

for i in range(1,n+1):
    for j in range(i+1, n+1):
        start_x, start_y = node[i]
        end_x, end_y  = node[j]
        cost = math.sqrt((start_y-end_y) ** 2 + (start_x-end_x) ** 2)
        graph.append((i,j,cost))

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

answer, counter = 0,0
for i in range(m):
    a,b = map(int, input().split())
    if find(a) != find(b):
        union(a,b)

graph.sort(key= lambda x:x[2])

for a,b,c in graph :
    if find(a) != find(b):
        answer += c
        counter += 1
        union(a,b)
        if counter == n - 1:
            break
print(f"{answer:.2f}")