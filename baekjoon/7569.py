from collections import deque

queue = deque()
move = [(0,0,-1),(0,0,1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

x, y, z = map(int, input().split())
m = []
for i in range(z) :
    temp = []
    for j in range(y) :
        temp.append(list(map(int, input().split())))
    m.append(temp)


for i in range(z) :
    for j in range(y) :
        for k in range(x) :
            if m[i][j][k] == 1 :
                queue.append((i,j,k,0))
answer = 0
while queue :
    now_z, now_y, now_x, count = queue.popleft()
    answer = max(answer, count)
    for i in move :
        move_z, move_y, move_x = i
        move_z, move_y, move_x = now_z+move_z, now_y+move_y, now_x+move_x
        if 0 <= move_z < z and 0 <= move_y < y and 0 <= move_x < x :
            if m[move_z][move_y][move_x] == 0 :
                m[move_z][move_y][move_x] = 1
                queue.append((move_z,move_y,move_x,count+1))

for i in range(z) :
    for j in range(y) :
        for k in range(x) :
            if m[i][j][k] == 0 :
                answer = -1
print(answer)