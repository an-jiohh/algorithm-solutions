n, m = map(int, input().split())
visited = [False] * (n + 1)
answer = []

def dfs(depth):
    if depth == m :
        print(*answer)
        return
    for i in range(1, n+1):
        if visited[i] == False :
            visited[i] = True
            answer.append(i)
            dfs(depth+1)
            visited[i] = False
            answer.pop()
dfs(0)