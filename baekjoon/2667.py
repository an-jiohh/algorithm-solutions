from collections import deque

move = [(0,1),(0,-1),(1,0),(-1,0)]

n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]


def dfs(y,x) :
    queue = deque([(y,x)])
    arr[y][x] = 0
    count = 0
    while queue :
        now_y, now_x = queue.pop()
        count += 1
        for move_y, move_x in move :
            move_y, move_x = move_y+now_y, move_x+now_x
            if 0 <= move_y < n and 0 <= move_x < n :
                if arr[move_y][move_x] == 1 :
                    arr[move_y][move_x] = 0
                    queue.append((move_y,move_x))
    return count

answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 :
            answer.append(dfs(i,j))
answer.sort()
print(len(answer))
for i in answer :
    print(i)