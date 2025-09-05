# s지점에서 출발
# 목적지 후보들 중 하나가 그들의 목적지
# 목적지까지 우회하지 않고 최단거리

"""
# 같은 길이의 ‘g–h를 지나는’ 경로가 나중에 발견돼도 dist가 더 작지 않으면 갱신되지 않음
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

Testcase = int(input())

for T in range(Testcase):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n+1)]
    check = [False] * (n+1)
    dist = [10 ** 9] * (n+1)
    target = []
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    for i in range(t):
        target.append(int(input()))
    queue = [(0,s,s)]
    dist[s] = 0
    while queue :
        c, sv, ev = heappop(queue)
        if dist[ev] < c :
            continue
        if (sv == g and ev == h) or (sv == h and ev == g) :
            check[ev] = True
        if check[sv] : check[ev] = True
        for nv, nc in graph[ev]:
            if dist[nv] > c + nc :
                dist[nv] = c + nc
                heappush(queue, (c+nc, ev, nv))
    answer = []
    for i in target:
        if check[i] and dist[i] < 10 ** 9: 
            answer.append(i)
    answer.sort()
    print(*answer)
"""

## 다익스트라는 생각보다 빠르다
## O((V+E log(V)))
## V+E = n으로 치환했을때 1,000,000도 가능
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

Testcase = int(input())

for T in range(Testcase):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n+1)]
    target = []
    gh_cost = 0
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
        if (a == g and b == h) or (a == h and b == g): gh_cost = d
    for i in range(t):
        target.append(int(input()))
    def dsk(start):
        dist = [10 ** 9] * (n+1)
        queue = [(0,start)]
        dist[start] = 0
        while queue :
            c, v = heappop(queue)
            if dist[v] < c :
                continue
            for nv, nc in graph[v]:
                if dist[nv] > c + nc :
                    dist[nv] = c + nc
                    heappush(queue, (c+nc, nv))
        return dist
    start_s = dsk(s)
    start_h = dsk(h)
    start_g = dsk(g)
    answer = []
    for i in target:
        s_h_g_t = start_s[h] + gh_cost + start_g[i]
        s_g_h_t = start_s[g] + gh_cost + start_h[i]
        if start_s[i] == s_h_g_t or start_s[i] == s_g_h_t :
            answer.append(i)
    answer.sort()
    print(*answer)

