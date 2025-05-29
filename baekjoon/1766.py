# n개의 문제, 1 ~ n까지 갈수록 문제어려워짐
# N개의 문제는 모두 풀어야 한다.
# 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 가능하면 쉬운문제 부터 풀어야한다.
# 위상정렬을 사용하여 풀이하되, 전체를 순회하면서 진입차수가 0인 노드부터 넣으면 2번째 조건을 해결할 수 있으며, 
# 전체를 작은 번호부터 시작하기 때문에, 3번째 조건도 해결가능
# 1번조건도 결국에 진입점이 없는 문제도 모두 순회하기 때문에 결국에 풀게됨
# 이럴 떄문제는 순환그래프처럼 계속 서클링이되는 경우라면?? -> 진입차수를 계속해서 뺴기 때문에 서클링 문제도 해결됨(위상정렬 개념)
from collections import deque
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edge = [[] for _ in range(n+1)] #방향 저장 배열
dp = [0] * (n + 1) #진입차수 저장 배열

for i in range(m):
    a,b = map(int, input().split())
    edge[a].append(b)
    dp[b] += 1

heap_queue = []
for i in range(1, n+1):
    if dp[i] == 0 : heap_queue.append(i)

heapq.heapify(heap_queue)
answer = []
while heap_queue :
    temp = heapq.heappop(heap_queue)
    answer.append(temp)
    for j in edge[temp] :
        dp[j] -= 1
        if dp[j] == 0 :
            heapq.heappush(heap_queue, j)
print(*answer)