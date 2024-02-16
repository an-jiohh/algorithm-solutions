from collections import deque

n = int(input())

img = [list(input()) for i in range(n)]
bg_img = []

move = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(n) :
    temp = img[i][:]
    for j in range(n) :
        if temp[j] == "R" :
            temp[j] = "G"
    bg_img.append(temp)

def bfs(starty, startx, img) :
    queue = deque([[starty,startx]])
    color = img[starty][startx]
    img[starty][startx] = 0
    while queue :
        y, x = queue.popleft()
        for k in move :
            my, mx = k
            if 0 <= y + my < n and 0 <= x + mx < n :
                if img[y + my][x + mx] == color :
                    img[y + my][x + mx] = 0
                    queue.append([y + my,x + mx])


count = 0
bg_count = 0
for i in range(n) :
    for j in range(n) :
        if img[i][j] != 0 :
            bfs(i, j, img)
            count += 1
        if bg_img[i][j] != 0 :
            bfs(i,j,bg_img)
            bg_count += 1

print(count, bg_count)
