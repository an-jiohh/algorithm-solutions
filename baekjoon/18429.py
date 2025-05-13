n, k = map(int, input().split())

a = list(map(int, input().split()))
visited = [False] * n
answer = 0

def dfs(w, count) :
    global answer
    if w < 500 :
        return
    if count == n :
        answer += 1
        return
    for i in range(n):
        if visited[i] == False :
            visited[i] = True
            dfs(w - k + a[i], count + 1)
            visited[i] = False


dfs(500, 0)
print(answer)