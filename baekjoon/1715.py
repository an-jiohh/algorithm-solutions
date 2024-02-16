import heapq
import sys

input = sys.stdin.readline

queue = []
answer = 0

n = int(input())

for i in range(n) :
    queue.append(int(input()))

heapq.heapify(queue)

while len(queue) > 1 :
   a,b = heapq.heappop(queue), heapq.heappop(queue)
   answer += (a+b)
   heapq.heappush(queue,  a+b)

print(answer)