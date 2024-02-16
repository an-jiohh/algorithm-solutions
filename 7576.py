from collections import deque

X, Y = map(int, input().split())

box = []
count = 0

for i in range(Y) :
    box.append(list(map(int, input().split())))

queue = deque()

for i in range(Y) :
    for j in range(X) :
        if box[i][j] == 1 :
            queue.append([i, j, 0])
position = [[-1,0],[1,0],[0,-1],[0,1]]

while queue :
    y, x, count = queue.popleft()
    for i in position :
        addx, addy = i
        if 0 <= x + addx < X and 0 <= y + addy < Y :
            if box[y + addy][x + addx] == 0 :
                box[y + addy][x + addx] = 1
                queue.append([y+addy, x+ addx, count+1])

def checkBlank() :
    for i in range(Y) :
        for j in range(X) :
            if box[i][j] == 0 :
                return True
    return False

if checkBlank() :
    print(-1)
else :
    print(count)