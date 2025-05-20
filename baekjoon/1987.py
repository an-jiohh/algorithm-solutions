r, c = map(int, input().split())

arr = []

for _ in range(r):
    arr.append(list(input()))

visited = [True] * (ord("Z") - ord("A")+ 1)
visited[ord(arr[0][0]) - ord("A")] = False 
move = [(0,1),(0,-1),(1,0),(-1,0)]
answer = 0
def dfs(y, x, count):
    global answer
    answer = max(count, answer)
    for position in move :
        move_y, move_x = position
        if 0 <= y+move_y < r and 0 <= x+move_x < c :
            target = ord(arr[y+move_y][x+move_x]) - ord("A")
            if visited[target]:
                visited[target] = False
                dfs(y+move_y,x+move_x, count+1)
                visited[target] = True

dfs(0,0,1)
print(answer)