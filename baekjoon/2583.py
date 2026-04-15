m, n, k = map(int, input().split())

graph = [[0] * n for i in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
    
from collections import deque

next_node = [(0, 1),(0, -1),(1,0),(-1,0)]

def bfs(y, x):
    queue = deque([(y,x)])
    area_sum = 1
    graph[y][x] = 1
    while queue :
        now_y, now_x = queue.popleft()
        for next_y, next_x in next_node :
            next_y, next_x = next_y + now_y, next_x + now_x
            if 0 <= next_y < m and 0 <= next_x < n :
                if graph[next_y][next_x] == 0 :
                    graph[next_y][next_x] = 1
                    area_sum += 1
                    queue.append((next_y, next_x)) 
    return area_sum
answer = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 :
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
print(*answer)