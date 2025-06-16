# 자손에 대한 정보가 주어질때, 가장 나라를 세운 사람과 혈통이 가까운 사람을 찾는 프로그램을 만드는 문제

from collections import deque


n, m = map(int, input().split())

graph = {}
increase = {}
blood = {}

king = input()

people = set()
for i in range(n):
   c, p1, p2 = input().split()
   graph[p1] = graph.get(p1, [])
   graph[p1].append(c)
   graph[p2] = graph.get(p2, [])
   graph[p2].append(c)
   increase[c] = increase.get(c, 0) + 2
   people.update([c,p1,p2])

queue = deque()

for i in people :
   if increase.get(i, 0) == 0 :
    blood[i] = 0
    queue.append(i)
blood[king] = 1.0

while queue :
   node = queue.popleft()
   for child in graph.get(node, []):
      blood[child] = blood.get(child, 0) + blood[node] / 2
      increase[child] -= 1
      if increase[child] == 0:
         queue.append(child)

answer = []
for i in range(m):
   temp = input()
   answer.append((blood.get(temp, 0), temp))

answer.sort(reverse=True)
print(answer[0][1])