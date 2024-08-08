from collections import deque
import copy

n, m = map(int, input().split())

location = [list(map(int, input().split())) for _ in range(n)]
move = [(0,1),(1,0),(-1,0),(0,-1)]

start = []
answer = n*m
count_full_safe = 0

for y in range(n) :
    for x in range(m) :
        if location[y][x] == 2 :
            start.append((y,x))
        if location[y][x] == 0 :
            count_full_safe += 1

def dfs(count) :
    global answer
    if count == 3 :
        answer = min(bfs() + count, answer)
        return
    for y in range(n) :
        for x in range(m) :
            if location[y][x] == 0 :
                location[y][x] = 1
                dfs(count+1)
                location[y][x] = 0
def bfs():
    count = 0
    queue = deque(start)
    check_location = copy.deepcopy(location)
    while queue :
        y,x = queue.popleft()
        for move_y, move_x in move :
            if 0 <= y+move_y < n and 0 <= x+move_x < m : 
                if check_location[y+move_y][x+move_x] == 0 :
                    check_location[y+move_y][x+move_x] = 2
                    queue.append((y+move_y,x+move_x))
                    count += 1
    return count
            
dfs(0)
print(count_full_safe - answer)