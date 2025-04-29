n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
answer = []

def dfs(start, next):
    visited[next] = True
    if visited[arr[next]] == False :
        dfs(start, arr[next])
    elif start == arr[next] :
        answer.append(start)
        return

for i in range(1,n+1):
    visited = [False] * (n+1)
    dfs(i, i)

print(len(answer))
answer.sort()
for i in answer :
    print(i)