# 실패 이유 1 : 100번째 수 미포함
# 실패 이유 2 : 비가 안올 경우도 예외 케이스로 포함시켜야함

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

m = [list(map(int, input().split())) for i in range(n)]
move = [(0,1),(0,-1),(1,0),(-1,0)]

answer = 0
for t in range(0,101):
    count = 0
    visited = [[False] *n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if m[y][x] <= t : visited[y][x] = True
    for ty in range(n):
        for tx in range(n):
            if visited[ty][tx] : continue
            visited[ty][tx] = True
            queue = deque([(ty,tx)])
            count += 1
            while queue:
                y,x = queue.popleft()
                for move_y, move_x in move:
                    move_y, move_x = y + move_y, x + move_x
                    if 0 <= move_y < n and 0 <= move_x < n and not visited[move_y][move_x]:
                        visited[move_y][move_x] = True
                        queue.append((move_y, move_x))
    answer = max(answer, count)
print(answer)