import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

people = input().split()
graph = {}
increase = {}
child = {}
answer = {}
master = []
visited = {}

for i in people :
    increase[i] = 0
    child[i] = 0
    graph[i] = []
    answer[i] = []
    visited[i] = False

m = int(input())

for i in range(m):
    a,b = input().split()
    graph[b].append(a)
    increase[a] += 1
    child[a] += 1

queue = deque()
for i in graph:
    if increase[i] == 0 :
        queue.append(i)
        master.append(i)

while queue :
    node = queue.popleft()
    for i in graph[node]:
        increase[i] -= 1
        if increase[i] == 0:
            answer[node].append(i)
            queue.append(i)

master.sort()
people.sort()
print(len(master))
print(*master)
for i in people :
    print(i, len(answer[i]), *sorted(answer[i]))