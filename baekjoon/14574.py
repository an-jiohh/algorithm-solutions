# n명이 둘씩 요리 대결, 승리자를 천국
# 한명만 남으면 해당 요리사는 지옥
# n명, 각 요리실력 p, 인기도 c
# 시청률은 c,p 공식으로 이루어짐
# n-1경기 동안, 시청률의 총합을 최대화 경기가 어떻게 진행되어야하는지?

# 경기 = 노드간의 간선
# 패자만 다시 대결 = 승자는 다시 포함되지 않게 해야하는데
# 노드간의 연산을 진행하는 프림이 어울려보임

import sys
sys.setrecursionlimit(10**9)

n = int(input())

arr = [list(map(int,input().split()))for i in range(n)]

graph = []

for i in range(n):
    p1,c1 = arr[i]
    for j in range(i+1, n):
        p2,c2 = arr[j]
        cost = (c1+c2) // abs(p1-p2)
        graph.append((i,j,cost))

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

graph.sort(key=lambda x:-x[2])

answer_list = [[] for _ in range(n)]
answer, count = 0,0
for a,b,c in graph :
    if find(a) != find(b) :
        union(a,b)
        answer += c
        answer_list[a].append(b)
        answer_list[b].append(a)
        count += 1
        if count == n-1:
            break
print(answer)

win_list = []
visited = [False] * n
def dfs(cur):
    for nxt in answer_list[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)
            print(cur + 1, nxt + 1)  # 패자, 승자


root = find(0)
visited[root] = True
dfs(root)
