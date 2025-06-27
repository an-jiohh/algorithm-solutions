# U, D, L, R
# 성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직임
# 특정 지점에 ‘SAFE ZONE’ 성우의 피리소리를 피하게함
# 최소 개수의 ‘SAFE ZONE’
# 어느 구역에 있더라도 SAFE ZONE’의 최소 개수를 구하는 문제

"""
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int,input().split())

arr = [list(input()) for i in range(n)]

parent = {}

for i in range(n):
    for j in range(m):
        parent[(i,j)] = (i,j)

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

visited = [[False] * m for i in range(n)]
start = (0,0)

direction = { "D": (1,0), "U":(-1,0), "L":(0,-1), "R":(0,1)}

def dfs(y,x):
    next_arrow = arr[y][x]
    next_y, next_x = y + direction[next_arrow][0],x + direction[next_arrow][1]
    if 0 <= next_y < n and 0 <= next_x < m :
        union((y,x), (next_y, next_x))
        if not visited[next_y][next_x] :
            visited[next_y][next_x] = True
            dfs(next_y, next_x)


for i in range(n):
    for j in range(m):
        if not visited[i][j] :
            visited[i][j] = True
            dfs(i,j)

answer = {}
for i in range(n):
    for j in range(m):
        answer[find((i,j))] = True

print(len(answer))
"""

import sys
sys.setrecursionlimit(10**9)

n, m = map(int,input().split())

arr = [list(input()) for i in range(n)]

parent = {}

for i in range(n):
    for j in range(m):
        parent[(i,j)] = (i,j)

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

direction = { "D": (1,0), "U":(-1,0), "L":(0,-1), "R":(0,1)}

answer = 0
for i in range(n):
    for j in range(m):
            dy, dx = direction[arr[i][j]]
            next_y, next_x = i + dy,j + dx
            if find((i,j)) == find((next_y, next_x)):
                answer += 1
            union((i,j), (next_y,next_x))
print(answer)