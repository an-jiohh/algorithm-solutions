n, m = map(int, input().split())

arr = [input() for _ in range(n)]
from collections import deque

queue = deque([(0,0,1)])

direction = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[0]*m for _ in range(n)]

while queue :
    y,x,count = queue.popleft()
    if y==n-1 and x == m-1 :
        print(count)
        break
    for move_y, move_x in direction :
        if 0 <= x+move_x < m and 0<=y+move_y < n :
            if arr[y+move_y][x+move_x]=="1" and visited[y+move_y][x+move_x] == 0:
                visited[y+move_y][x+move_x] = 1
                queue.append((y+move_y,x+move_x,count+1))
