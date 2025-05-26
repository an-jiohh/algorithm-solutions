# n*n 공간
# m 마리 물고기
# 처음 아기상어 크기는 2
# 아기상어는 상하좌우로 움직임, 자신의 크기보다 작은 물고기만 가능
# 크기가 크면 못지나감, 같거나 작으면 지나갈 수 있음
# 먹을 수 있는 물고기로 이동, 가까운 물고기부터(위, 왼쪽, 아래, 오른쪽)
# ---
# 풀이
# visited로 탐색위치 저장 = 같거나 작을경우 지나갈 수 있음을 처리하기 위해
# 가장 가까운 = bfs로 주변부터 탐색, 찾으면 이동할 위치 반환, 먹이먹는 처리
# 위를 계속해서 반복하되 / 아기상어가 다른 먹이를 먹을 방법이 없는 경우
# bfs탐색 이후 이동할 노드가 없을때 = 이동할 위치가 없을때 초기 위치를 반환하여 처리
from collections import deque

move = [(-1,0),(0,-1),(1,0),(0,1)] # y,x기준 위, 왼쪽, 아래, 오른쪽

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

start_y, start_x = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start_y, start_x = i, j
            arr[start_y][start_x] = 0


def bfs(shark, y,x):
    queue = deque([(y,x,0)])
    visited = set((y,x))
    end = []
    while queue :
        y, x, time = queue.popleft()
        for i in move:
            move_y, move_x = y + i[0], x + i[1]
            if 0 <= move_y < n and 0 <= move_x < n and (move_y, move_x) not in visited :
                if 0 < arr[move_y][move_x] < shark :
                    #기존 코드
                    #return(move_y,move_x, time+1) #조건이 제일위, 왼쪽이므로 전체를 탐색 후 
                    end.append((move_y, move_x, time + 1)) #조건이 제일위, 왼쪽이므로
                elif arr[move_y][move_x] <= shark : 
                    visited.add((move_y, move_x))
                    queue.append((move_y,move_x,time+1))
    if not end : return (-1,-1,-1)
    else : 
        end.sort(key=lambda x:(x[2],x[0],x[1]))
        return end[0]

shark, level_count = 2, 2
answer = 0
while True :
    start_y, start_x, time = bfs(shark, start_y, start_x)
    if time == -1 : break
    arr[start_y][start_x] = 0
    level_count -= 1
    if level_count == 0 :
        shark += 1
        level_count = shark
    answer += time
print(answer)
