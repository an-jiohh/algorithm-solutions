import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

d = [(0,1), (1, 0), (0, -1), (-1, 0),(1,1),(-1,-1),(-1,1),(1,-1)]

global w, h, m, visited

def dfs(x, y):
    m[y][x] = 0
    for temp in d :
        dy, dx = temp
        if 0 <= x + dx < w and 0 <= y + dy < h :
            if m[y+dy][x+dx] == 1 :
                dfs(x+dx, y+dy)

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    m = [list(map(int, input().split())) for _ in range(h)]
    answer = 0
    for i in range(w):
        for j in range(h):
            if m[j][i] :
                dfs(i, j)
                answer += 1
    print(answer)
