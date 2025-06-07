# 여러가지 부품으로 조립
# 기본 부품 -> 중간 부품, 기본부품은 다른 부품으로 조립될 수 없는 부품
# 중간 부품 = 중간부품또는 기본부품으로 생산
# 예시) 중간 부품 5는 2개의 기본 부품 1, 2개의 기본 부품 2로 만들어짐
# 기본 부품의 종류별 개수를 계산하는 프로그램을 작성
# 1 ~ n-1까지는 중간기본부품, n은 완제품
# 자연수 m = x,y,k -> x를 만드는데 y가 k개 필요함
# 중간에 위상정렬하며 필요한 부품을 배열에 저장(간선간에 가중치가 있는것으로 생각) -> 모든 부품으로 착각
# 처음 생각나는 방법, 필요한 기본 부품을 배열로 저장함

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
increase = [0] * (n+1)
parts = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x,y,k = map(int, input().split())
    graph[y].append((x,k))
    increase[x] += 1

queue = deque()
for i in range(1,n+1):
    if increase[i] == 0 :
        queue.append(i)
        parts[i][i] = 1

while queue :
    node = queue.popleft()
    for i in graph[node]:
        x, k = i
        increase[x] -= 1
        for j in range(1,n+1):
            parts[x][j] += parts[node][j] * k
        if increase[x] == 0 :
            queue.append(x)

for i in range(1,n+1):
    if parts[n][i] != 0 :
        print(i, parts[n][i])