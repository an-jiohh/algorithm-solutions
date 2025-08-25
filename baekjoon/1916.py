from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

visitied = [False] * (n+1)
dist = [10**9] * (n+1)
queue = [(0, start)] #heapq에서 작은 값을 꺼내기 위해 값저장

while queue :
    d, v = heappop(queue)
    if visitied[v] :
        continue
    visitied[v] = True
    for b,c in graph[v] :
        if dist[b] > d + c :
            dist[b] = d + c
            heappush(queue, (d+c, b))

print(dist[end])