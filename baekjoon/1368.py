"""import sys

input = sys.stdin.readline

n = int(input())

cost = [int(input()) for i in range(n)]
graph = []

answer = 0
for i in range(n):
    temp = list(map(int, input().split()))
    m = 10 ** 9
    for j in temp :
        if j != 0 and m > j : m = j
    if m < cost[i] :
        for j in range(i+1, n):
            graph.append((i, j, temp[j]))
            graph.append((j, i, temp[j]))
    else :
        answer += cost[i]
        cost[i] = 10 ** 9

answer += min(cost)

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

graph.sort(key= lambda x:x[2])

count = 0
for a,b,c in graph :
    if find(a) != find(b) :
        union(a,b)
        count += 1
        answer += c
        if count == n - 1 :
            break
print(answer)"""

import sys

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(1,n+1): #가상노드
    cost = int(input())
    graph.append((0, i, cost))

answer = 0
for i in range(1,n+1):
    temp = list(map(int, input().split()))
    for j in range(1,n+1):
        if i != j :
            graph.append((i, j, temp[j-1]))

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

graph.sort(key= lambda x:x[2])

count = 0
for a,b,c in graph :
    if find(a) != find(b) :
        union(a,b)
        count += 1
        answer += c
        if count == n :
            break
print(answer)
