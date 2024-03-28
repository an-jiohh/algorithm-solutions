from collections import deque

move = [(0,1),(0,-1),(1,0),(-1,0)]
n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(y, x, visited) :
    queue = deque([(y,x)])
    visited[y][x] = 1
    target_sum = arr[y][x]
    target = [(y,x)]
    while queue :
        y,x = queue.pop()
        node_num = arr[y][x]
        for move_y, move_x in move:
            move_y, move_x = move_y+y, move_x+x
            if 0 <= move_y < n and 0 <= move_x < n and visited[move_y][move_x] == 0:
                if l <= abs(arr[move_y][move_x] - node_num) <= r :
                    target_sum += arr[move_y][move_x]
                    target.append((move_y,move_x))
                    queue.append((move_y,move_x))
                    visited[move_y][move_x] = 1
    target_aver = target_sum // len(target)
    for target_y, target_x in target :
        arr[target_y][target_x] = target_aver


answer = -1
while True :
    visited = [[False] * n for _ in range(n)]
    check = n * n
    answer += 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False :
                bfs(i, j, visited)
                check -= 1
    if check == 0 :
        break
print(answer)