n = int(input())

t = []
p = []

for i in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

answer = 0
def dfs(start, value):
    global answer
    if start == n :
        answer = max(answer, value)
        return
    elif start > n :
        return
    
    dfs(start+1, value)
    dfs(start+t[start], value+p[start])
dfs(0,0)
print(answer)