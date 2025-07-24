# 네트워크에 고장이 발생하더라도 컴퓨터들이 연결되어 있도록 안정적인 네트워크를 구축
# 이들은 본사의 메인 컴퓨터와 직접 연결되어 있다. +  본사의 컴퓨터는 항상 1번 컴퓨터이다.
# 고장 유형
# 1. 두 컴퓨터의 연결이 끊어지는 경우 -> 다른 컴퓨터들을 경유하여 연결
# 2. 컴퓨터가 고장 나는 경우 -> 고장 나지 않은 컴퓨터들끼리 연결

# 1. 연결이 끊어지는 경우
# case1 임의의 컴퓨터가 1번(본사)와 연결이 끊어지는 경우 : 다른 컴퓨터와 연결
# case2 임의의 컴퓨터가 다른 컴퓨터와 연결이 끊어지는 경우 : 1번은 모두 연결되어 있어 1번을 경우해서 연결되어짐, 고려 X

# 2. 컴퓨터가 고장 나는 경우 
# case1 : 1번(본사)의 컴퓨터가 고장나는 경우 : 다른 모든 노드들이 연결
# case2 : 임의의 컴퓨터가 고장나는 경우 : 1번은 모두 연결되어 있어 1번을 경유해서 연결되어짐, 고려 X

# 1번을 제외한 나머지 노드들의 최소 스패닝 트리가 형성된다면 조건을 맞출 수 있음

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y :
        parent[root_y] = root_x
        return 1
    return 0

count = 0
for i in range(m):
    a, b = map(int, input().split())
    count += union(a,b)

cost = [list(map(int, input().split())) for i in range(n)]

graph = []


for i in range(2,n+1):
    for j in range(i+1,n+1):
        graph.append((i,j,cost[i-1][j-1]))

graph.sort(key=lambda x:x[2])

answer, answer_list = 0, []
for a,b,c in graph :
    if find(a) != find(b):
        union(a,b)
        answer += c
        answer_list.append((a,b))
        count += 1
        if count == n-2:
            break
print(answer, len(answer_list))
for i in answer_list :
    print(*i)

# 실패이유
# M개의 간선이 전부 다른 집합에 속해있는 두 노드를 이어주는 것이 아님 -> 같은 집합에 속한 두 노드를 이어줄 수도 있음
# count += union(a,b)으로 성공만 카운트하여 해결