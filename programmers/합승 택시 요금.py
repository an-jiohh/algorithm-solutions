# 경우의 수 확인
# 데익스트라 1번
# s -> a, b
# 데익스트라 2번
# s -> a -> b, s -> b -> a
# s -> ? -> a, b 
# 데익스트라 3번
# s -> ? -> a -> b, s -> ? -> b -> a

# 3번의 경우에는 2번 s -> ? -> a,b로 자동으로 포함됨
# 2번 s -> a -> b의 경우에 s -> ? -> a,b 경우에 포함될 수 있음

from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for i in range(n+1)]
    for start,end,cost in fares:
        graph[start].append((cost,end))
        graph[end].append((cost,start))
        
    def dijkstra(start):
        diff = [10**9] * (n+1)
        diff[start] = 0
        queue = [(0, start)]
        while queue :
            c, v = heappop(queue)
            if diff[v] < c :
                continue
            for nc, nv in graph[v] :
                if diff[nv] > c + nc :
                    diff[nv] = c + nc
                    heappush(queue, (c+nc, nv))
        return diff
    
    all_cost = [dijkstra(i) for i in range(n+1)]
    answer = all_cost[s][a] + all_cost[s][b]
    for i in range(1,n+1):
        answer = min(answer, all_cost[s][i] + all_cost[i][a] + all_cost[i][b])
    return answer