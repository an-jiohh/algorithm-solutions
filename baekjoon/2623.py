# m명의 피디가 가수 순서를 가져온다
# 이순서에 맞도록 전체 가수의 순서를 구하는 문제
# 순서를 만들 수 없는 경우 0을 출력
# 순서를 만들 수 없는 경우 = pd들이 순서를 서로 반대로 가져올경우? = 위상정렬시 사이클이 발생하는 경우
# 위상 정렬시 사이클이 발생하는 경우 = n개가 모두 정렬되지 못하는 경우
# 왜? 사이클이 형성되어있는 경우 사이클 때문에 차수가 빠지지 않아, 전체를 순회할 수 없음

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
increase = [0] * (n+1)

for i in range(m):
    arr = list(map(int, input().split()))
    start= arr[1]
    for end in arr[2:] :
        graph[start].append(end)
        increase[end] += 1
        start = end

queue = deque()
for i in range(1,n+1):
    if increase[i] == 0 :
        queue.append(i)
answer = []

while queue :
    node = queue.popleft()
    answer.append(node)
    for i in graph[node]:
        increase[i] -= 1
        if increase[i] == 0 :
            queue.append(i)

if len(answer) == n :
    for i in answer :
        print(i)
else :
    print(0)