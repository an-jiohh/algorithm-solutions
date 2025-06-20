# 섬으로 이루어진 나라가 있고, 모든 섬을 다리로 연결
# 섬은 연결된 땅이 상하좌우로 붙어있는 덩어리
# 다리의 방향은 가로 또는 세로, 중간에 바꿀 수 없음
# 다리의 길이는 2 이상
from collections import deque

n, m = map(int, input().split())

island = [list(map(int, input().split()))for i in range(n)]

dir = [(0,1),(0,-1),(1,0),(-1,0)]

visited = [[False] * m for i in range(n)]
queue = deque()

island_count = 2
for i in range(n):  # 2부터 네이밍
    for j in range(m):
        if island[i][j] == 1 and not visited[i][j] :
            visited[i][j] = True
            island[i][j] = island_count
            queue.append((i,j))
            while queue :
                y, x = queue.popleft()
                for d_y, d_x in dir :
                    d_y, d_x = d_y + y, d_x + x
                    if 0 <= d_y < n and 0 <= d_x < m :
                        if island[d_y][d_x] == 1 and not visited[d_y][d_x] :
                            island[d_y][d_x] = island_count
                            visited[d_y][d_x] = True
                            queue.append((d_y,d_x))
            island_count += 1

graph = set()


for i in range(n):
    check, ex_island, count = 0, 0, 0
    for j in range(m):
        if check != island[i][j] : #값이 바뀔때
            if check == 0 and island[i][j] != 0 : #이전이 바다이고, 이전 섬이 있었을때 = 다리 건설 중
                if ex_island != 0 and count >= 2:
                    graph.add((ex_island, island[i][j], count))
            count = 0
            ex_island = check
        count += 1
        check = island[i][j]

for j in range(m):
    check, ex_island, count = 0, 0, 0
    for i in range(n):
        if check != island[i][j] : #값이 바뀔때
            if check == 0 and island[i][j] != 0 : #이전이 바다이고, 이전 섬이 있었을때 = 다리 건설 중
                if ex_island != 0 and count >= 2:
                    graph.add((ex_island, island[i][j], count))
            count = 0
            ex_island = check
        count += 1
        check = island[i][j]

graph = list(graph)

parent = [i for i in range(island_count+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x

graph.sort(key=lambda x:x[2])
graph_count, answer = 0, 0
for a,b,c in graph :
    if find(a) != find(b) :
        union(a,b)
        answer += c
        graph_count += 1
        if graph_count == island_count - 3 :
            break
if graph_count != island_count - 3:
    answer = -1
print(answer)