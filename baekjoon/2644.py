n = int(input())

a, b = map(int, input().split())

m = int(input())

arr = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


answer = -1
not_visited = [True] * (n + 1)
def dfs(node, count):
    global answer
    if node == b :
        answer = count
        return
    not_visited[node] = False
    for i in arr[node] :
        if not_visited[i] :
            dfs(i, count+1)
dfs(a, 0)
print(answer)