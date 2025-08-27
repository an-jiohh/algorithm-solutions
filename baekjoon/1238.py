# 단방향 그래프
# N명의 학생들이 N개의 도시에 있음
# 파티가 열리는 X로 갔다가 다시 돌아와야함

# 다익스트라는 a -> 나머지 도시로 가는 최단거리를 구하는 문제
# 다시 돌아갈때는 파티장소에서 -> n개의 도시로 이동하는 경우 1번만 구하면됨
# 즉 모든 경우를 시작으로 다익스트라 -> 이후 갈때 올때의 거리를 구해 주면됨
from heapq import heappush, heappop

n,m,x = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(s) :
    dist = [10 ** 9] * (n+1)
    dist[s] = 0
    queue = [(0,s)]
    while queue:
        c, v = heappop(queue)
        if c < dist[v] :
            continue
        for nv, nc in graph[v]:
            if dist[nv] > c + nc :
                dist[nv] = c + nc
                heappush(queue, (c+nc, nv))
    return dist

dij_list = []

for i in range(n+1):
    dij_list.append(dijkstra(i))

answer = [0] * (n+1)
for i in range(1, n+1):
    answer[i] = dij_list[i][x] + dij_list[x][i]
print(max(answer))