import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 10 ** 9
move = [(0,1),(1,0),(-1,0),(0,-1)]
count = 1

while True :
    n = int(input())
    if n == 0 : break

    m = [list(map(int, input().split())) for i in range(n)]
    dist = [[INF] * n for i in range(n)]
    queue = [(m[0][0],0,0)] #cost, y, x
    dist[0][0] = m[0][0]
    while queue :
        cost, y, x = heappop(queue)
        if dist[y][x] < cost :
            continue
        for my, mx in move :
            my, mx = y + my, x + mx
            if 0 <= my < n and 0 <= mx < n :
                if dist[my][mx] > cost + m[my][mx] :
                    dist[my][mx] = cost + m[my][mx]
                    heappush(queue, (cost + m[my][mx], my, mx))
    print(f"Problem {count}: {dist[n-1][n-1]}")
    count += 1