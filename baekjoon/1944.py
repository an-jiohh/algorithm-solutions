# 복제 장치를 이용하면 자기 자신을 똑같은 로봇으로 원하는 개수만큼 복제
# 로봇의 임무는 미로에 흩어진 열쇠들을 모두 찾는 것
# 열쇠가 있는 곳들과 로봇이 출발하는 위치에 로봇이 복제 장치
# 모든 열쇠를 찾으면서 로봇이 움직이는 횟수의 합을 최소로 하는 프로그램을 작성
# 로봇이 한 번 지나간 자리라도 다른 로봇 또는 자기 자신이 다시 지나갈 수 있음
#

# 5 2
# K11K1
# 00001
# 11011
# 1S011
# 11111

# Answer: 10
# BFS만 사용하였을때 위의 예시 때문에 정답을 찾지못한다. K가 아닌 곳에서 분할되기 때문
from collections import deque

n, m = map(int, input().split())

arr = [list(input()) for i in range(n)]

node = []
node_num = {}

for i in range(n):
    for j in range(n):
        if arr[i][j] == "S" or arr[i][j] == "K" :
            node_num[(i,j)] = len(node)
            node.append((i,j))

next_xy = [(0,1),(0,-1),(1,0),(-1,0)]

graph = []

for i in range(len(node)):
    visited = [[False] * n for i in range(n)]
    y, x = node[i]
    queue = deque([(y,x,0)])
    visited[y][x] = True
    while queue :
        y, x, cost = queue.popleft()
        for next_x, next_y in next_xy :
            next_y, next_x = y + next_y, x + next_x
            if 0 <= next_y < n and 0 <= next_x < n and not visited[next_y][next_x] and arr[next_y][next_x] != "1":
                visited[next_y][next_x] = True
                queue.append((next_y, next_x, cost+1))
                if (next_y, next_x) in node_num :
                    index = node_num[(next_y,next_x)]
                    graph.append((i, index, cost+1))

parent = [i for i in range(len(node))]

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

graph.sort(key=lambda x:x[2])
answer, count = 0, 0
for a,b,cost in graph:
    if find(a) != find(b) :
        union(a,b)
        answer += cost
        count += 1
        if count == len(node)-1:
            break
if count != len(node) - 1:
    answer = -1
print(answer)