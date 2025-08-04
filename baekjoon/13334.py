# 지금 보고있는 사람을 기준으로 오른쪽 좌표를 기준으로
# 그 안에 들어올 수 있는 사람들만 큐에 남김
# 큐 크기가 정답

import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    if a < b : arr.append((a,b))
    else : arr.append((b,a))
l = int(input())

arr.sort(key=lambda x:x[1])

queue = []
answer = 0

for next_h, next_o in arr:
    if next_o-next_h > l : continue
    while queue and queue[0][0] < next_o - l:
            heapq.heappop(queue)
    heapq.heappush(queue, (next_h, next_o))
    
    answer = max(answer, len(queue))
print(answer)
