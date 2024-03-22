import sys

input = sys.stdin.readline

move = [(0,-1),(0,1),(1,0),(-1,0)]

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for i in range(m)]

def dfs(y,x,pre) :
    answer = 0
    if y == m-1 and x == n-1 :
        return 1
    if dp[y][x] != -1 :
        return dp[y][x]
    for move_y, move_x in move :
        move_y, move_x = y+move_y, x+move_x
        if 0 <= move_y < m and 0 <= move_x < n :
            if arr[move_y][move_x] < pre :
                answer += dfs(move_y,move_x,arr[move_y][move_x])
    dp[y][x] = answer
    return answer
print(dfs(0,0,arr[0][0]))