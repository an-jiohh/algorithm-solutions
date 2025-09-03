from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n, e = map(int ,input().split())

graph = [[] for i in range(n+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

def dikstra(start, target) :
    dist= [10 ** 9] * (n+1)
    queue = [(0,start)]
    dist[start] = 0
    while queue :
        c,v = heappop(queue)
        if dist[v] < c :
            continue
        for nv, nc in graph[v] :
            if dist[nv] > c + nc :
                dist[nv] = c + nc
                heappush(queue, (c+nc, nv))
    return dist[target]

first_v1 = dikstra(1,v1) + dikstra(v1,v2) + dikstra(v2,n)
first_v2 = dikstra(1,v2) + dikstra(v2,v1) + dikstra(v1,n)
answer = min(first_v1, first_v2)

# 1,v1 = INF, 부분집합이 이동 불가능할때 = INF + ? 이므로 >으로 모두 포함되게
# v1 = 1, v2 = n 일때
# (가능할때) -> 본인을 찾음으로 함수 반환값으로 본인을 ㅂ반환
# (불가능할때) -> 딱 INF값을 반환함으로 =으로 INF가 포함되도록 
if answer >= 10 ** 9 :
    answer = -1

print(answer)