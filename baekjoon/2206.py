from collections import deque

move = [(0,1),(0,-1),(1,0),(-1,0)]

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0]*m for i in range(n)] 

answer = -1
queue = deque([(0,0,1,0)]) #y좌표, x좌표, 이동횟수, 벽을 뿌셨는지 체크
while queue :
    y,x,count,check = queue.popleft()
    if y == n-1 and x == m-1 : 
        answer = count
        break
    for move_y, move_x in move :
        move_y, move_x = y+move_y, x+move_x
        if 0 <= move_y < n and 0 <= move_x < m:
            if check == 1 and visited[move_y][move_x] >= 1:
                continue
            if check == 0 and visited[move_y][move_x] == 1:
                continue
            visited[move_y][move_x] = 1 + check
            if arr[move_y][move_x] != 1 :
                queue.append((move_y,move_x,count+1,check)) 
            elif check == 0 :
                queue.append((move_y,move_x,count+1,1))
print(answer)